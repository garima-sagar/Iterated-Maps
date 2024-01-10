def logistic_map(x, r):
    return r * x * (1 - x)

def char_to_num(char):
    return ord(char) - ord('A')  # Map 'A' to 0, 'B' to 1, ..., 'Z' to 25

def num_to_char(num):
    return chr(num + ord('A'))  # Map 0 to 'A', 1 to 'B', ..., 25 to 'Z'

def encrypt(message, r):
    encrypted_message = []
    x = 0.5  # Initial condition for the logistic map
    for char in message:
        num = char_to_num(char)
        x = logistic_map(x, r)
        encrypted_num = (num + int(x * 100)) % 26  # Encrypt the numerical value
        encrypted_char = num_to_char(encrypted_num)
        encrypted_message.append(encrypted_char)
    return ''.join(encrypted_message)

# Example usage:
message = "HELLO"
encryption_parameter = 3.9  # You can choose a different parameter
encrypted_message = encrypt(message, encryption_parameter)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
