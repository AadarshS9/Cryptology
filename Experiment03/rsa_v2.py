#RSA ALGORITHM SIMPLER
import math

p = int(input("Enter a prime number p: "))
q = int(input("Enter a prime number q: "))
n = p * q
print("n =", n)
phi = (p - 1) * (q - 1)

e = 2
while e < phi:
    if math.gcd(e, phi) == 1:
        break
    else:
        e += 1

print("e =", e)
k = 2
d = ((k * phi) + 1) // e
print("d =", d)

print(f'Public key: (e={e}, n={n})')
print(f'Private key: (d={d}, n={n})')

msg = int(input("Enter a plaintext message (integer): "))
print(f'Original message: {msg}')

C = pow(msg, e)
C = C % n
print(f'Encrypted message: {C}')

M = pow(C, d)
M = M % n

print(f'Decrypted message: {M}')
