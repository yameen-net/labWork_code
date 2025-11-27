import os
import csv
import hashlib



folder_path = os.path.dirname(os.path.abspath(__file__))
test_files_path = os.path.join(folder_path, "test_files")
baseline_path = os.path.join(folder_path, "baseline.csv")

# LOAD THE BASELINE
# im creating a dictionary to store the "good" hashes from the CSV
# Format will be: {'filename': 'hash_string'}
known_files = {}

try:
    with open(baseline_path, 'r') as f:
        reader = csv.reader(f)
        
        # Skip the first row because its just headers 
        next(reader)
        
        for row in reader:
            filename = row[0]
            saved_hash = row[1]
            known_files[filename] = saved_hash
            
except FileNotFoundError:
    print("Error: Could not find baseline.csv. Did you run section 1?")
    exit()

print("--- Checking File Integrity ---")

#  SCAN THE FOLDER
# Get list of current files
current_files = os.listdir(test_files_path)

for filename in current_files:
    file_path = os.path.join(test_files_path, filename)

    if os.path.isfile(file_path):
        
        # calculating the hash 
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as f:

            content = f.read()
            hasher.update(content)
        
        current_hash = hasher.hexdigest()
        
        # COMPARE WITH BASELINE
        if filename in known_files:
          
            original_hash = known_files[filename]
            
            if current_hash == original_hash:
                print(f"[OK] {filename} is safe.")
            else:
                print(f"[ALERT] {filename} has been MODIFIED!")
                
            # Remove from list so we can track deleted files later
            del known_files[filename]
            
        else:
            # File is on disk but not in  CSV
            print(f"[ALERT] {filename} is a NEW file (possible malware).")

# CHECK FOR DELETED FILES
# Any files left in 'known_files' were not found in the folder
for missing_file in known_files:
    print(f"[ALERT] {missing_file} has been DELETED!")