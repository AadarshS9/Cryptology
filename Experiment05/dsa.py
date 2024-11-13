#DSA
!pip install cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def generate_keys():
    private_key = dsa.generate_private_key(key_size=2048, backend=default_backend())
    public_key = private_key.public_key()

    private_bytes = private_key.private_bytes(encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,encryption_algorithm=serialization.NoEncryption())

    public_bytes = public_key.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo)
    return private_bytes, public_bytes

def sign_message(private_key_bytes, message):
    private_key = serialization.load_pem_private_key(private_key_bytes,password=None,backend=default_backend())
    signature = private_key.sign(message,hashes.SHA256())
    return signature

def verify_signature(public_key_bytes, message, signature):
    public_key = serialization.load_pem_public_key(public_key_bytes,backend=default_backend())
    try:
        public_key.verify(signature,message,hashes.SHA256())
        print("Signature is valid.")
    except Exception:
        print("Signature is invalid.")

private_key, public_key = generate_keys()
message = input("Enter a message to sign using DSA: ")
message = message.encode('utf-8')
signature = sign_message(private_key, message)
print(f"Signature: {signature.hex()}")
verify_signature(public_key, message, signature)
