import string
import math

COMMON_PASSWORDS = {
    "password", "Password", "PASSWORD", "123456", "123456789", "12345678"
}

def analyze_password(pw: str):

    length = len(pw)

    #checking for different types of characters

    has_lower = any(c.islower() for c in pw)
    has_upper = any(c.isupper() for c in pw)
    has_digit = any(c.isdigit() for c in pw)
    has_symbol = any(c in string.punctuation for c in pw)

    #checking for length

    length_pts = 0
    if length >= 8:
        length_pts += 1
    if length >= 12:
        length_pts += 1

    # Variety points

    variety_pts = sum([has_lower, has_upper, has_digit, has_symbol])


     # pool size for entropy: sum sets that appear in the password
    pool_size = 0
    if has_lower:
        pool_size += 26
    if has_upper:
        pool_size += 26
    if has_digit:
        pool_size += 10
    if has_symbol:
        pool_size += len(string.punctuation)

    # working out entropy
    entropy_bits = 0.0
    if pool_size > 0 and length > 0:
        entropy_bits = length * math.log2(pool_size)

    #penalising common passworkds

    is_common = pw.lower() in COMMON_PASSWORDS
    penalty = 3 if is_common else 0


    score = length_pts + variety_pts - penalty

    # bonus for randomness
    if entropy_bits >= 60:
        score += 1
    if entropy_bits >= 80:
        score += 1

    # calculating scores
    score = max(0, min(10, score))



     # Verdict based on score
    if score <= 3:
        verdict = "Very Weak"
    elif score <= 5:
        verdict = "Weak"
    elif score <= 7:
        verdict = "Okay"
    elif score <= 9:
        verdict = "Strong"
    else:
        verdict = "Excellent"


    return {
    "password_length": length,
    "length_points": length_pts,
    "variety_points": variety_pts,
    "has_lower": has_lower,
    "has_upper": has_upper,
    "has_digit": has_digit,
    "has_symbol": has_symbol,
    "pool_size": pool_size,
    "entropy_bits": round(entropy_bits, 2),
    "is_common_password": is_common,
    "score_out_of_10": score,
    "verdict": verdict

        }
    

passToTest = input("Enter a password to test: ")
result = analyze_password(passToTest)
print(f"\nScore: {result['score_out_of_10']} ({result['verdict']})")
print(f"Entropy: {result['entropy_bits']} bits")
print(f"Details: length={result['password_length']}, "
        f"variety_points={result['variety_points']}, "
        f"common={result['is_common_password']}")