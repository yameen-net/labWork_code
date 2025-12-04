password = input("Enter password: ")

#special characters
special_characters = set("@#$%^&*()-_+=[]{}|\\:;\"'<>,.?/")

# Create a list to store unmet criteria
errors = []

# Check each criterion
if len(password) < 8:
    errors.append("at least 8 characters long")

if not any(char.isupper() for char in password):
    errors.append("at least one uppercase letter")

if not any(char.islower() for char in password):
    errors.append("at least one lowercase letter")
    
if not any(char in special_characters for char in password):
    errors.append("at least one special character")

# Print the results
if not errors:
    print("Password is strong")
else:
    print("Password must contain " + ", ".join(errors) + ".")
