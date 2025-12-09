

# if a computer makes more than 3 connections it is suspicious
THRESHOLD_LIMIT = 3 

# Simulate Network Traffic Logs
# Here, I am listing (Source IP -> Destination IP)
network_traffic_logs = [
    ["192.168.1.5", "192.168.1.10"], # User 5 is browsing normal stuff
    ["192.168.1.5", "192.168.1.11"],
    ["192.168.1.20", "192.168.1.2"],  # User 20 is working normally
    
    # Now, here is the infected machine 
    ["192.168.1.99", "192.168.1.1"],
    ["192.168.1.99", "192.168.1.2"],
    ["192.168.1.99", "192.168.1.3"],
    ["192.168.1.99", "192.168.1.4"],
    ["192.168.1.99", "192.168.1.5"]
]

print("--- Starting Network Traffic Analysis ---")

# 3. Count connections for each IP
# I am using a dictionary to keep score
connection_counts = {}

for record in network_traffic_logs:
    source_ip = record[0]
    
    # If we haven't seen this IP before, add it to the list with count 0
    if source_ip not in connection_counts:
        connection_counts[source_ip] = 0
    
    # Add 1 to their connection count
    connection_counts[source_ip] = connection_counts[source_ip] + 1

# 4. Check for anomalies (Rule-based detection)
print("Analyzing connection counts...")

for ip in connection_counts:
    count = connection_counts[ip]
    print("Host " + ip + " made " + str(count) + " connections.")
    
    if count > THRESHOLD_LIMIT:
        print("[ALERT] Anomaly Detected! Host " + ip + " is behaving suspiciously.")
        print("        Action: Logging event and notifying admin.")
        # In a real system, we might block the IP here
    else:
        print("        Status: Normal")

print("--- Analysis Complete ---")