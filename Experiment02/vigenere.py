# Vigenère Cipher
while True:
    choice = int(input("\n1. Encrypt\n2. Decrypt\n3. Exit\nChoose an option: "))

    if choice in [1, 2]:
        plaintext = input("Enter message: ").upper().replace(" ", "")
        key = input("Enter key: ").upper().replace(" ", "")
        extended_key = (key * ((len(plaintext) // len(key)) + 1))[:len(plaintext)]

        result_text = []
        for i in range(len(plaintext)):
            if choice == 1:
                char_code = (ord(plaintext[i]) + ord(extended_key[i])) % 26
            else:
                char_code = (ord(plaintext[i]) - ord(extended_key[i]) + 26) % 26

            result_text.append(chr(char_code + ord('A')))

        result_text = ''.join(result_text)

        if choice == 1:
            print("Encrypted Message:", result_text)
        else:
            print("Decrypted Message:", result_text)

    elif choice == 3:
        break
    else:
        print("Invalid choice. Please select a valid option.")
