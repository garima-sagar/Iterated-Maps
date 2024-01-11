def henon_map(x, y, a, b):
    new_x = 1 - a * x ** 2 + y
    new_y = b * x
    return new_x, new_y

def char_to_num(char):
    return ord(char) - ord('A')  # Map 'A' to 0, 'B' to 1, ..., 'Z' to 25

def num_to_char(num):
    return chr(num + ord('A'))  # Map 0 to 'A', 1 to 'B', ..., 25 to 'Z'

def encrypt(message, a, b):
    encrypted_message = []
    x, y = 0.1, 0.1  # Initial conditions for the Hénon map
    for char in message:
        num = char_to_num(char)
        x, y = henon_map(x, y, a, b)
        encrypted_num = (num + int(x * 100)) % 26  # Encrypt the numerical value
        encrypted_char = num_to_char(encrypted_num)
        encrypted_message.append(encrypted_char)
    return ''.join(encrypted_message)

# Example usage:
message = "HELLO"
henon_parameters = (1.4, 0.3)  # You can choose different parameters
encrypted_message = encrypt(message, *henon_parameters)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
