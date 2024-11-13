#Affine Cipher
def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b."""
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    """Find the modular inverse of a under modulo m."""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def validate_a(a):
    """Check if 'a' is coprime with 26."""
    if gcd(a, 26) != 1:
        print("Invalid value for 'a'. It must be coprime with 26.")
        return False
    return True

while True:
    choice = int(input("\n1. Encrypt\n2. Decrypt\n3. Exit\nChoose an option: "))

    if choice in [1, 2]:
        a = int(input("Enter key 'a' (must be coprime with 26): "))
        if not validate_a(a):
            continue

        b = int(input("Enter key 'b': "))

        plaintext = input("Enter message: ").upper().replace(" ", "")

        if choice == 1:
            cipher_text = ''
            for char in plaintext:
                if char.isalpha():
                    x = ord(char) - ord('A')
                    encrypted_char = (a * x + b) % 26
                    cipher_text += chr(encrypted_char + ord('A'))
            print("Encrypted Message:", cipher_text)

        elif choice == 2:
            plain_text = ''
            a_inv = mod_inverse(a, 26)
            if a_inv is None:
                print("Error: No modular inverse found, decryption not possible.")
                continue
            for char in plaintext:
                if char.isalpha():
                    y = ord(char) - ord('A')
                    decrypted_char = (a_inv * (y - b)) % 26
                    plain_text += chr(decrypted_char + ord('A'))
            print("Decrypted Message:", plain_text)

    elif choice == 3:
        break
    else:
        print("Invalid choice. Please select a valid option.")
