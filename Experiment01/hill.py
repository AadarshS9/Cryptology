# Hill Cipher without using functions
import numpy as np

n = int(input("Enter the size of the key matrix (e.g., 2 for 2x2, 3 for 3x3): "))
key = input(f"Enter {n*n}-letter key for the {n}x{n} matrix: ").upper().replace(" ", "")

key_matrix = []
for i in range(0, n*n, n):
    row = [ord(key[j]) - ord('A') for j in range(i, i + n)]
    key_matrix.append(row)

key_matrix = np.array(key_matrix)  # Convert list to a numpy array

det = int(np.round(np.linalg.det(key_matrix))) % 26
if det < 0:
    det += 26

det_inverse = None
for i in range(26):
    if (det * i) % 26 == 1:
        det_inverse = i
        break

if det == 0 or det_inverse is None:
    print("Invalid key matrix! It must be invertible under modulo 26.")
    exit()

while True:
    choice = int(input("\n1. Encrypt\n2. Decrypt\n3. Exit\nChoose an option: "))

    if choice in [1, 2]:
        msg = input("Enter message: ").upper().replace(" ", "")
        while len(msg) % n != 0:
            msg += 'X'

        msg_vector = []
        for i in range(0, len(msg), n):
            vector = [ord(msg[j]) - ord('A') for j in range(i, i + n)]
            msg_vector.append(vector)

        msg_vector = np.array(msg_vector)

        if choice == 2:
            adjugate = np.round(np.linalg.inv(key_matrix) * det).astype(int) % 26
            key_matrix = (det_inverse * adjugate).astype(int) % 26

        result = np.dot(msg_vector, key_matrix) % 26
        result_text = ''.join([chr(int(num) + ord('A')) for vector in result for num in vector])

        if choice == 1:
            print("Encrypted Message:", result_text)
        else:
            print("Decrypted Message:", result_text)

    elif choice == 3:
        break
    else:
        print("Invalid choice. Please select a valid option.")
