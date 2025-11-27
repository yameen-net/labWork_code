import os


# defining what to look out for

signatures = [
    "eval(",
    "base64.b64decode",
    "socket.connect",
    "exec(",
    "import os"
]

# 2. Get the path to the test_files folder
current_folder = os.path.dirname(os.path.abspath(__file__))
target_folder = os.path.join(current_folder, "test_files")

print("--- Starting Signature Scan ---")

# 3. LOOP THROUGH THE FILES
file_list = os.listdir(target_folder)

for filename in file_list:
    file_path = os.path.join(target_folder, filename)
    
    # We only want to scan files, not folders
    if os.path.isfile(file_path):
        
        try:
            # Open the file and read the text inside
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                
                # check if any of our bad signatures are in this file
                for sig in signatures:
                    if sig in content:
                        print(f"[ALERT] Found suspicious code '{sig}' in file: {filename}")
                        
        except Exception:
            
            print(f"Could not read {filename}")

print("--- Scan Complete ---")