from cryptography.fernet import Fernet

class Crypto:
    def __init__(self, key: str):
        self.key = key
        self.fernet = Fernet(key)

    def encrypt(self, content: str) -> str:
        return self.fernet.encrypt(content.encode()).decode()

    def decrypt(self, content: bytes) -> str:
        return self.fernet.decrypt(content).decode()