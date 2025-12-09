import re

sample = "C:/Users/moham/Downloads/ProcessMonitor/Procmon.exe"

def extract_strings(path):
    with open(path, "rb") as f:
        data = f.read()
    pattern = rb"[ -~]{4,}"
    return re.findall(pattern, data)
strings = extract_strings(sample)
for s in strings[:20]:
    print(s.decode(errors="ignore"))