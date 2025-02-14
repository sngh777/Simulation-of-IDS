import random
import numpy as np

# Simulate normal and attack traffic
data = []
for i in range(80):  # Normal traffic
    packet_size = random.uniform(100, 1500)  # Normal packet size range
    time_gap = random.uniform(50, 300)  # Normal time between packets in milliseconds
    failed_attempts = random.randint(0, 2)  # Rare failed logins for normal users
    data.append((i, [packet_size, time_gap, failed_attempts], 0))  # Label 0 (normal)

for i in range(20):  # Attack traffic
    packet_size = random.uniform(2000, 5000)  # Abnormally large packets
    time_gap = random.uniform(0, 10)  # Rapid succession (DDoS, brute force, etc.)
    failed_attempts = random.randint(3, 10)  # High number of failed logins (brute-force attack)
    data.append((i + 80, [packet_size, time_gap, failed_attempts], 1))  # Label 1 (attack)

random.shuffle(data)

# Compute normal traffic statistics
normal_features = np.array([features for _, features, label in data if label == 0])
mean, std = np.mean(normal_features, axis=0), np.std(normal_features, axis=0)

# Anomaly Detection Function using Z-score
def detect_anomaly(features, threshold=2.0):
    """Detect anomalies using Z-score."""
    return any(abs(f - m) / s > threshold for f, m, s in zip(features, mean, std))

# IDS Evaluation Function
def evaluate_ids():
    TP = FP = TN = FN = 0
    for _, features, actual in data:
        detected = detect_anomaly(features)
        if detected and actual: TP += 1
        elif detected and not actual: FP += 1
        elif not detected and not actual: TN += 1
        elif not detected and actual: FN += 1
    
    print(f"Precision: {TP / (TP + FP) if TP + FP else 0:.2f}")
    print(f"Recall: {TP / (TP + FN) if TP + FN else 0:.2f}")
    print(f"FPR: {FP / (FP + TN) if FP + TN else 0:.2f}")
    print(f"FNR: {FN / (FN + TP) if FN + TP else 0:.2f}")

# Run IDS evaluation
evaluate_ids()
