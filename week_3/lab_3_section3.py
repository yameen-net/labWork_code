import os, hashlib, base64

#pepper
PEPPER = os.environ.get("APP_PEPPER", "change-me-please")

def sha256_hex(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def make_salt(n_bytes=16) -> str:
    # Return base64 to make it easy to print/store
    return base64.b64encode(os.urandom(n_bytes)).decode()

# --- DEMO ---
if __name__ == "__main__":
    pwd = input("Enter a password (default: user123password): ").strip() or "user123password"
    print("\nSECTION 3: SALT & PEPPER")
    print("Password:", pwd, "\n")

    # 1) UNSALTED (BAD): same input = same hash
    h1 = sha256_hex(pwd.encode())
    h2 = sha256_hex(pwd.encode())
    print("1) Unsalted:")
    print("   hash #1:", h1)
    print("   hash #2:", h2)
    print("   identical? ->", h1 == h2, "\n")

    # 2) SALTED: same input but different random salts = different hashes
    s1 = make_salt()
    s2 = make_salt()
    h3 = sha256_hex(base64.b64decode(s1) + pwd.encode())
    h4 = sha256_hex(base64.b64decode(s2) + pwd.encode())
    print("2) salted")
    print("   salt #1:", s1)
    print("   hash #1:", h3)
    print("   salt #2:", s2)
    print("   hash #2:", h4)
    print("   identical hashes? ->", h3 == h4, "(should be False)\n")

    # 3) SALT + PEPPER: need DB (salt+hash) + separate secret (pepper)
    s3 = make_salt()
    h5 = sha256_hex(base64.b64decode(s3) + pwd.encode() + PEPPER.encode())
    print("3) salt + pepper ")
    print("   salt (store in DB):", s3)
    print("   hash (store in DB):", h5)
    print("   PEPPER is NOT stored in DB (keep in env/secret vault)\n")

