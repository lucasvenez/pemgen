from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

def generate_key_pair():
    # Generate an RSA key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    # Get the public key in PEM format
    public_key_pem = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Get the private key in PEM format
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    return public_key_pem, private_key_pem

def export_keys(public_key_pem, private_key_pem, public_key_file='public_key.pem', private_key_file='private_key.pem'):
    # Export public key to file
    with open(public_key_file, 'wb') as f:
        f.write(public_key_pem)

    # Export private key to file
    with open(private_key_file, 'wb') as f:
        f.write(private_key_pem)

# Generate key pair
public_key_pem, private_key_pem = generate_key_pair()

# Export keys to files
export_keys(public_key_pem, private_key_pem)

print("Public and private keys have been exported to 'public_key.pem' and 'private_key.pem'.")
