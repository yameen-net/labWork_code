

import string, math
import bcrypt, pyotp, qrcode
from pathlib import Path

# Database
USERS = {}  # username -> {"hash": bytes, "totp_secret": str}

# 
def is_strong(pw: str):
    if len(pw) < 8: 
        return False, "Use at least 8 characters."
    kinds = sum([
        any(c.islower() for c in pw),
        any(c.isupper() for c in pw),
        any(c.isdigit() for c in pw),
        any(c in string.punctuation for c in pw)
    ])
    if kinds < 3:
        return False, "Mix upper/lower/digits/symbols (at least 3 types)."
    # quick entropy-ish number 
    pool = (26 if any(c.islower() for c in pw) else 0) \
         + (26 if any(c.isupper() for c in pw) else 0) \
         + (10 if any(c.isdigit() for c in pw) else 0) \
         + (len(string.punctuation) if any(c in string.punctuation for c in pw) else 0)
    bits = 0 if pool == 0 else len(pw) * math.log2(pool)
    return True, f"~entropy ≈ {bits:.1f} bits (higher is better)."

# register user
def register_user(username: str, password: str, cost: int = 12):
    ok, msg = is_strong(password)
    if not ok:
        raise ValueError("Weak password: " + msg)

    # bcrypt 
    salt = bcrypt.gensalt(rounds=cost)
    pw_hash = bcrypt.hashpw(password.encode(), salt)

    # create TOTP secret for this user
    secret = pyotp.random_base32()
    USERS[username] = {"hash": pw_hash, "totp_secret": secret}

    # make provisioning URI and QR
    uri = pyotp.TOTP(secret).provisioning_uri(name=username, issuer_name="GoldAuth")
    out_path = Path(__file__).with_name(f"{username}_totp_qr.png")
    qrcode.make(uri).save(out_path)

    print("\n[REGISTERED]")
    print("User:", username)
    print("Password:", "(hidden, stored as bcrypt hash)")
    print("TOTP secret (store server-side):", secret)
    print("QR saved to:", out_path.resolve())
    print("Scan it with Google Authenticator/Authy.")
    return uri

# Login
def login(username: str, password: str, code: str) -> bool:
    user = USERS.get(username)
    if not user:
        print("No such user.")
        return False

    # 1) password check (bcrypt)
    if not bcrypt.checkpw(password.encode(), user["hash"]):
        print("Wrong password.")
        return False

    # 2) TOTP check
    totp = pyotp.TOTP(user["totp_secret"])
    if not totp.verify(code, valid_window=1):
        print("Wrong 2FA code.")
        return False

    return True


if __name__ == "__main__":
    print("SECTION 6: Complete Auth")

    # Register
    uname = input("Choose username [student01]: ").strip() or "student01"
    pw = input("Choose password   [MyP@ssw0rd123]: ").strip() or "MyP@ssw0rd123"

    try:
        register_user(uname, pw, cost=12)
    except ValueError as e:
        print(e)
        raise SystemExit(1)

    print("\nNow open the PNG file next to this script and scan it in your Authenticator app.")
    input("Press Enter when ready to test login...")

    # Login
    pw_try = input("Password: ").strip() or pw
    code = input("6-digit TOTP code: ").strip()

    ok = login(uname, pw_try, code)
    print("Login successful?" , ok)
