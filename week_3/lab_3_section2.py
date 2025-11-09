
import hashlib
import bcrypt
import time


pwd = input("Enter a password to test (or press Enter for default): ").strip()
if pwd == "":
    pwd = "MyPassw0rd123"

print("\n=== HASHING DEMO: MD5 vs SHA-256 vs bcrypt ===")
print(f"Testing password: {pwd}\n")

# MD5 
t0 = time.perf_counter()
md5_hash = hashlib.md5(pwd.encode("utf-8")).hexdigest()
t1 = time.perf_counter()
print("[MD5]")
print(" hash:", md5_hash)
print(f" time: {(t1 - t0) * 1000:.3f} ms\n")

# SHA-256 
t0 = time.perf_counter()
sha256_hash = hashlib.sha256(pwd.encode("utf-8")).hexdigest()
t1 = time.perf_counter()
print("[SHA-256]")
print(" hash:", sha256_hash)
print(f" time: {(t1 - t0) * 1000:.3f} ms\n")

#bcrypt

cost = 12
print(f"[bcrypt] (work factor = {cost})")
t0 = time.perf_counter()
salt = bcrypt.gensalt(rounds=cost)            # random salt + parameter bundle
bcrypt_hash = bcrypt.hashpw(pwd.encode("utf-8"), salt) 
t1 = time.perf_counter()
print(" hash:", bcrypt_hash.decode())
print(f" time: {(t1 - t0):.3f} s\n")



