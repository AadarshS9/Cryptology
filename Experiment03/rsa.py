#RSA ALGORITHM
import math

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi):
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("Inverse doesn't exist")
    else:
        return x % phi

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

d = mod_inverse(e, phi)
print("d =", d)

print(f'Public key: (e={e}, n={n})')
print(f'Private key: (d={d}, n={n})')

msg = int(input("Enter a plaintext message (integer): "))
print(f'Original message: {msg}')

C = pow(msg, e, n)
print(f'Encrypted message: {C}')

M = pow(C, d, n)
print(f'Decrypted message: {M}')
