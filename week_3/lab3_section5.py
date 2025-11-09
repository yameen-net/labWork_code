

import hashlib, time
try:
    import bcrypt
    HAS_BCRYPT = True
except ImportError:
    HAS_BCRYPT = False

# wordlist 
common_passwords = [
    "password", "123456", "qwerty", "letmein", "admin",
    "welcome", "iloveyou", "monkey", "dragon", "football",
    "abc123", "111111", "password1", "Passw0rd", "MyP@ssw0rd"
]

# Hash helpers 
def md5_hex(s: str) -> str:
    return hashlib.md5(s.encode()).hexdigest()

def sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()


def dict_attack_fast(target_hash: str, hash_type: str, words: list[str]):
    hfn = md5_hex if hash_type.lower() == "md5" else sha256_hex
    t0 = time.perf_counter()
    tries = 0
    for w in words:
        tries += 1
        if hfn(w) == target_hash:
            dt = time.perf_counter() - t0
            return True, w, tries, dt
    dt = time.perf_counter() - t0
    return False, None, tries, dt


if __name__ == "__main__":
    print("\n SECTION 5: DITCIONARY ATTACK DEMO ")
    #target password
    target_password = "MyP@ssw0rd"  

    # MD5 target & crack
    md5_target = md5_hex(target_password)
    ok, guess, tries, dt = dict_attack_fast(md5_target, "md5", common_passwords)
    print("\n[MD5] target_hash:", md5_target)
    print(f"[MD5] found={ok}, guess={guess}, tries={tries}, time={dt*1000:.3f} ms")

    # SHA-256 target & crack
    sha_target = sha256_hex(target_password)
    ok, guess, tries, dt = dict_attack_fast(sha_target, "sha256", common_passwords)
    print("\n[SHA-256] target_hash:", sha_target)
    print(f"[SHA-256] found={ok}, guess={guess}, tries={tries}, time={dt*1000:.3f} ms")

    
