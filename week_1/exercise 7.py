def caesar_cipher(message, key, mode):
    result = ""
    
    # cahnging key for decryption mode
    if mode.lower() == "decrypt":
        key = -key

    for char in message:
        # Process uppercase letters
        if char.isupper():
            shifted = (ord(char) - ord('A') + key) % 26 + ord('A')
            result += chr(shifted)
        # Process lowercase letters
        elif char.islower():
            shifted = (ord(char) - ord('a') + key) % 26 + ord('a')
            result += chr(shifted)

        # leaving special chars unchangedd
        else:
            result += char
    return result

# Example 
message = input("Enter message: ")
key = int(input("Enter key (number of positions): "))
mode = input("Enter mode (encrypt/decrypt): ")

output = caesar_cipher(message, key, mode)
print("Output:", output)