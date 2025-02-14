import random
import numpy as np

# Generate normal and attack traffic
data = [(i, [random.uniform(0, 0.6) for _ in range(3)], 0) for i in range(80)] + \
       [(i+80, [random.uniform(0.7, 1.0) for _ in range(3)], 1) for i in range(20)]
random.shuffle(data)

# Compute normal traffic statistics
normal_features = np.array([features for _, features, label in data if label == 0])
mean, std = np.mean(normal_features, axis=0), np.std(normal_features, axis=0)

# Explanation of Z-score:
# Z-score measures how far a value is from the average (mean) in terms of standard deviation.
# A high Z-score means the value is very different from normal data, which may indicate an anomaly.

def detect_anomaly(features, threshold=2.0):
    """Detect anomalies using Z-score."""
    return any(abs(f - m) / s > threshold for f, m, s in zip(features, mean, std))

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
