import hashlib
import bcrypt

def md5_hash(password):
    return hashlib.md5(password.encode()).hexdigest()

def sha256_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

def bcrypt_hash(password, rounds=12):
    # bcrypt.gensalt creates a random salt and includes the cost
    salt = bcrypt.gensalt(rounds)
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

def bcrypt_check(password, stored_hash):
    return bcrypt.checkpw(password.encode(), stored_hash.encode())

def main():
    print("=== Simple Password Hashing Demo ===")
    pw = input("Enter a password to hash: ")

    md5_h = md5_hash(pw)
    sha_h = sha256_hash(pw)
    b_h = bcrypt_hash(pw)  # bcrypt includes its salt inside the result

    print("\nHashes:")
    print("MD5:     ", md5_h)
    print("SHA-256: ", sha_h)
    print("bcrypt:  ", b_h)

    # show bcrypt generates different hash each time (because of random salt)
    b_h2 = bcrypt_hash(pw)
    print("\nbcrypt again (different because salt changes):")
    print("bcrypt #2:", b_h2)

    # verification example
    attempt = input("\nRe-enter password to verify against first bcrypt hash: ")
    if bcrypt_check(attempt, b_h):
        print("Login: success ✅")
    else:
        print("Login: failure ❌")

if __name__ == "__main__":
    main()