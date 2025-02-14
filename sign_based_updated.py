import random

# Define attack signatures (known malicious patterns)
attack_signatures = [
    {"src_ip": "192.168.1.100", "dst_port": 22, "payload_size": 5000},  # SSH brute-force
    {"src_ip": "10.0.0.5", "dst_port": 80, "payload_size": 8000},       # Large HTTP attack
    {"src_ip": "172.16.2.50", "dst_port": 443, "payload_size": 10000},  # Large HTTPS DDoS
]

# Generate simulated network traffic
def generate_traffic(num_packets=100):
    data = []
    for i in range(num_packets):
        packet = {
            "src_ip": f"192.168.1.{random.randint(1, 255)}",
            "dst_port": random.choice([22, 80, 443, 53, 3306]),
            "payload_size": random.randint(100, 10000),
        }
        label = 1 if packet in attack_signatures else 0  # Label as attack (1) if it matches signature
        data.append((i, packet, label))
    return data

# Signature-based detection function
def detect_signature(packet):
    """Check if a packet matches any known attack signature."""
    return packet in attack_signatures

# Evaluate IDS performance
def evaluate_signature_ids():
    data = generate_traffic()
    TP = FP = TN = FN = 0
    
    for _, packet, actual in data:
        detected = detect_signature(packet)
        if detected and actual: TP += 1
        elif detected and not actual: FP += 1
        elif not detected and not actual: TN += 1
        elif not detected and actual: FN += 1

    print(f"Signature-Based IDS Performance:")
    print(f"Precision: {TP / (TP + FP) if TP + FP else 0:.2f}")
    print(f"Recall: {TP / (TP + FN) if TP + FN else 0:.2f}")
    print(f"False Positive Rate (FPR): {FP / (FP + TN) if FP + TN else 0:.2f}")
    print(f"False Negative Rate (FNR): {FN / (FN + TP) if FN + TP else 0:.2f}")

# Run IDS evaluation
evaluate_signature_ids()
