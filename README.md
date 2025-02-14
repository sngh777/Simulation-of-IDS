# Intrusion Detection System (IDS)

## **What are the 3 values in feature level?**
Each network traffic sample in our IDS is represented by **three numerical features**:
1. **Packet Size** – The amount of data transmitted in a packet.
2. **Time Interval** – The time gap between consecutive packets.
3. **Protocol-Specific Metric** – A characteristic related to the protocol used (e.g., HTTP request size, TCP flag count).

These features are used to analyze patterns and detect abnormal behaviors in network traffic.

---

## **What is Feature Level?**
Feature level refers to the specific attributes extracted from raw network traffic data to **represent its behavior numerically**.
These extracted values allow machine learning models or rule-based systems to classify whether a given packet or connection is normal or malicious.

---

## **Feature-Level Representation of Network Traffic**
Each network traffic sample is represented as:
```python
(index, [feature_1, feature_2, feature_3], label)
```
Where:
- `index`: Unique identifier for the sample.
- `[feature_1, feature_2, feature_3]`: Feature vector representing network traffic behavior.
- `label`: `0` for normal traffic, `1` for attack traffic.

Example:
```python
(5, [0.23, 0.75, 0.33], 0)   # Normal traffic
(12, [0.91, 0.45, 0.87], 1)  # Attack traffic
```
---

## **Signature-Based IDS Implementation**
A **signature-based IDS** identifies malicious activity by comparing network traffic against a predefined list of known attack signatures.

### **How It Works:**
1. A list of known attack signatures is created.
2. Incoming packets are checked against these signatures.
3. If a match is found, the packet is flagged as an attack.
4. If no match is found, the packet is considered normal.

### **Example Signature Format:**
```python
attack_signatures = [
    {"src_ip": "192.168.1.100", "dst_port": 22, "payload_size": 5000},
    {"src_ip": "10.0.0.5", "dst_port": 80, "payload_size": 8000},
    {"src_ip": "172.16.2.50", "dst_port": 443, "payload_size": 10000},
]
```

### **Detection Mechanism:**
For each incoming packet, the IDS checks if it matches an attack signature.
```python
def detect_signature(packet):
    return packet in attack_signatures
```
If a match is found, the IDS raises an alert for potential intrusion.

---
This README provides an overview of **anomaly-based** and **signature-based IDS** with feature-level representation. 🚀

