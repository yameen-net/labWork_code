import os
import hashlib
import csv
import time

def generate_baseline(directory, output_csv):
    with open(output_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Filename", "Hash", "Timestamp"])
        
        # Loop through files in the directory
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                # Create SHA-256 hash 
                sha256_hash = hashlib.sha256()
                with open(filepath, "rb") as f:
                    # Read file in chunks to avoid memory issues
                    for byte_block in iter(lambda: f.read(4096), b""):
                        sha256_hash.update(byte_block)
                
                writer.writerow([filename, sha256_hash.hexdigest(), time.ctime()])

generate_baseline('test_files', 'baseline.csv')