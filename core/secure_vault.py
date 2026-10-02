import base64
import hashlib

class SecureVault:
    @staticmethod
    def encrypt_payload(data_string, secret_salt="AetherHPCSupremeKey"):
        key = hashlib.sha256(secret_salt.encode()).hexdigest()
        encoded_chars = []
        for i in range(len(data_string)):
            key_c = key[i % len(key)]
            encoded_c = chr(ord(data_string[i]) ^ ord(key_c))
            encoded_chars.append(encoded_c)
        encrypted_data = "".join(encoded_chars)
        return base64.urlsafe_b64encode(encrypted_data.encode()).decode()
