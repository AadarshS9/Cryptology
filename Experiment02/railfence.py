# Rail Fence Cipher

while True:
    choice = int(input("\n1. Encrypt\n2. Decrypt\n3. Exit\nChoose an option: "))

    if choice in [1, 2]:
        plaintext = input("Enter message: ").replace(" ", "")
        key = int(input("Enter numeric key (number of rails): "))

        if key <= 1 or key >= len(plaintext):
            print("Invalid key! It must be greater than 1 and less than the length of the message.")
            continue

        rail_matrix = [['\n' for _ in range(len(plaintext))] for _ in range(key)]

        if choice == 1:
            row, direction = 0, 1
            for i in range(len(plaintext)):
                rail_matrix[row][i] = plaintext[i]
                if row == 0:
                    direction = 1
                elif row == key - 1:
                    direction = -1
                row += direction

            cipher_text = ''.join([''.join(row) for row in rail_matrix if row])
            print("Encrypted Message:", cipher_text)

        elif choice == 2:
            row, direction = 0, 1
            for i in range(len(plaintext)):
                rail_matrix[row][i] = '*'
                if row == 0:
                    direction = 1
                elif row == key - 1:
                    direction = -1
                row += direction

            idx = 0
            for r in range(key):
                for c in range(len(plaintext)):
                    if rail_matrix[r][c] == '*' and idx < len(plaintext):
                        rail_matrix[r][c] = plaintext[idx]
                        idx += 1

            row, direction = 0, 1
            plain_text = []
            for i in range(len(plaintext)):
                plain_text.append(rail_matrix[row][i])
                if row == 0:
                    direction = 1
                elif row == key - 1:
                    direction = -1
                row += direction

            print("Decrypted Message:", ''.join(plain_text))

    elif choice == 3:
        break
    else:
        print("Invalid choice. Please select a valid option.")
