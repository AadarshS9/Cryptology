# Playfair Cipher
key = input("Enter key: ").replace(" ", "").upper().replace('J', 'I')

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

matrix = [matrix[i:i + 5] for i in range(0, 25, 5)]

while True:
    choice = int(input("\n1. Encrypt\n2. Decrypt\n3. Exit\nChoose an option: "))

    if choice in [1, 2]:
        msg = input("Enter message: ").replace(" ", "").upper().replace('J', 'I')

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

        if len(digraphs[-1]) == 1:
            digraphs[-1] += 'X'

        result = []

        for digraph in digraphs:
            for row in range(5):
                if digraph[0] in matrix[row]:
                    row1, col1 = row, matrix[row].index(digraph[0])
                if digraph[1] in matrix[row]:
                    row2, col2 = row, matrix[row].index(digraph[1])

            if col1 == col2:
                if choice == 1:
                    result.append(matrix[(row1 + 1) % 5][col1])
                    result.append(matrix[(row2 + 1) % 5][col2])
                else:
                    result.append(matrix[(row1 - 1) % 5][col1])
                    result.append(matrix[(row2 - 1) % 5][col2])
            elif row1 == row2:
                if choice == 1:
                    result.append(matrix[row1][(col1 + 1) % 5])
                    result.append(matrix[row2][(col2 + 1) % 5])
                else:
                    result.append(matrix[row1][(col1 - 1) % 5])
                    result.append(matrix[row2][(col2 - 1) % 5])
            else:
                result.append(matrix[row1][col2])
                result.append(matrix[row2][col1])

        result_text = ''.join(result)
        if choice == 1:
            print("Encrypted Message:", result_text)
        else:
            print("Decrypted Message:", result_text)

    elif choice == 3:
        break
    else:
        print("Invalid choice. Please select a valid option.")
