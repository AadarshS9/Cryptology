#PLAYFAIR CIPHER
def create_matrix(key):
    key = key.replace(" ", "").upper().replace('J', 'I')

    seen_chars = set()
    matrix = []
    for c in key:
        if c not in seen_chars:
            seen_chars.add(c)
            matrix.append(c)

    for i in range(65, 91):
        char = chr(i)
        if char == 'J':
            continue
        if char not in seen_chars:
            seen_chars.add(char)
            matrix.append(char)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def find_position(char, matrix):
    if char == 'J':
        char = 'I'
    for row in range(5):
        if char in matrix[row]:
            return row, matrix[row].index(char)
    return None

def process_digraphs(msg):
    msg = msg.replace(" ", "").upper().replace('J', 'I')
    digraphs = []
    i = 0

    while i < len(msg):
        char1 = msg[i]
        char2 = msg[i + 1] if (i + 1) < len(msg) else 'X'

        if char1 == char2:
            digraphs.append(char1 + 'X')
            i += 1
        else:
            digraphs.append(char1 + char2)
            i += 2

    if len(digraphs[-1]) == 1:  # Ensure the last digraph is complete
        digraphs[-1] += 'X'

    return digraphs

def encrypt_message(msg, matrix):
    digraphs = process_digraphs(msg)
    cipher_text = []

    for digraph in digraphs:
        row1, col1 = find_position(digraph[0], matrix)
        row2, col2 = find_position(digraph[1], matrix)

        if col1 == col2:  # Same column
            cipher_text.append(matrix[(row1 + 1) % 5][col1])
            cipher_text.append(matrix[(row2 + 1) % 5][col2])
        elif row1 == row2:  # Same row
            cipher_text.append(matrix[row1][(col1 + 1) % 5])
            cipher_text.append(matrix[row2][(col2 + 1) % 5])
        else:  # Rectangle swap
            cipher_text.append(matrix[row1][col2])
            cipher_text.append(matrix[row2][col1])

    return ''.join(cipher_text)

def decrypt_message(msg, matrix):
    digraphs = [msg[i:i + 2] for i in range(0, len(msg), 2)]
    plain_text = []

    for digraph in digraphs:
        row1, col1 = find_position(digraph[0], matrix)
        row2, col2 = find_position(digraph[1], matrix)

        if col1 == col2:  # Same column
            plain_text.append(matrix[(row1 - 1) % 5][col1])
            plain_text.append(matrix[(row2 - 1) % 5][col2])
        elif row1 == row2:  # Same row
            plain_text.append(matrix[row1][(col1 - 1) % 5])
            plain_text.append(matrix[row2][(col2 - 1) % 5])
        else:  # Rectangle swap
            plain_text.append(matrix[row1][col2])
            plain_text.append(matrix[row2][col1])

    return ''.join(plain_text)

def main():
    key = input("Enter key: ")
    matrix = create_matrix(key)

    while True:
        choice = int(input("\n1. Encrypt\n2. Decrypt\n3. Exit\nChoose an option: "))

        if choice == 1:
            message = input("Enter message to encrypt: ")
            cipher_text = encrypt_message(message, matrix)
            print("Encrypted Message:", cipher_text)
        elif choice == 2:
            cipher_text = input("Enter cipher text to decrypt: ")
            plain_text = decrypt_message(cipher_text, matrix)
            print("Decrypted Message:", plain_text)
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
