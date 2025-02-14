import random

# Define known attack signatures (example: sequence of feature patterns that indicate an attack)
signature_database = [
    [0.9, 0.8, 0.7],  # Example attack signature 1
    [0.85, 0.75, 0.65],  # Example attack signature 2
    [0.95, 0.9, 0.85]  # Example attack signature 3
]

# Simulated traffic dataset: (traffic_id, features, is_attack)
data = [(i, [random.uniform(0, 1) for _ in range(3)], random.choice([0, 1])) for i in range(100)]  # 0: Normal, 1: Attack

def signature_based_ids(features):
    """Signature-based IDS that checks if a packet matches known attack patterns."""
    for signature in signature_database:
        if all(abs(f - s) < 0.1 for f, s in zip(features, signature)):
            return True  # Attack detected
    return False  # No attack detected

# Performance Metrics
TP, FP, TN, FN = 0, 0, 0, 0

def classify_traffic():
    global TP, FP, TN, FN
    for packet_id, features, actual_attack in data:
        detected = signature_based_ids(features)
        if detected and actual_attack:
            TP += 1  # Correct attack detection
        elif detected and not actual_attack:
            FP += 1  # False positive
        elif not detected and not actual_attack:
            TN += 1  # Correct normal classification
        elif not detected and actual_attack:
            FN += 1  # False negative

    # Print Results
    print(f"True Positives: {TP}")
    print(f"False Positives: {FP}")
    print(f"True Negatives: {TN}")
    print(f"False Negatives: {FN}")

    # Compute Metrics
    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    fpr = FP / (FP + TN) if (FP + TN) > 0 else 0
    fnr = FN / (FN + TP) if (FN + TP) > 0 else 0
    
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"False Positive Rate: {fpr:.2f}")
    print(f"False Negative Rate: {fnr:.2f}")

# Run the classification simulation
classify_traffic()
