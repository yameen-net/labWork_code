import hashlib
import pefile

def compute_hash(path, algorithm):
    h = hashlib.new(algorithm)
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


sample = "C:/Users/moham/Downloads/ProcessMonitor/Procmon.exe"

# print("MD5: ", compute_hash(sample, "md5"))
# print("SHA1: ", compute_hash(sample, "sha1"))
# print("SHA256:", compute_hash(sample, "sha256"))


# --- STRING EXTRACTION ---

import re
def extract_strings(path):
    with open(path, "rb") as f:
        data = f.read()
    pattern = rb"[ -~]{4,}"
    return re.findall(pattern, data)
strings = extract_strings(sample)
for s in strings[:20]:
    print(s.decode(errors="ignore"))




pe = pefile.PE(sample)
print("Entry Point:", hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint))
print("Image Base:", hex(pe.OPTIONAL_HEADER.ImageBase))
print("\nImported DLLs and functions:")
for entry in pe.DIRECTORY_ENTRY_IMPORT:
    print(" ", entry.dll.decode())
for imp in entry.imports[:5]:
    print(" -", imp.name.decode() if imp.name else "None")
