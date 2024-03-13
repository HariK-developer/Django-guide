from cryptography.fernet import Fernet
from dotenv import dotenv_values

config = dotenv_values(".env")

SECRET_KEY = config.get("SECRET_KEY")


fernet = Fernet(SECRET_KEY)

def encrypt_data(data):
    """_summary_

    Args:
        data (_type_): _description_

    Returns:
        _type_: _description_
    """
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data):
    """_summary_

    Args:
        encrypted_data (_type_): _description_

    Returns:
        _type_: _description_
    """
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data