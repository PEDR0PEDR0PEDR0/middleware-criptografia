# services/crypto_service.py

import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Importa a chave Base64 do arquivo de configuração
try:
    from config import ENCRYPTION_KEY_B64
    # CORREÇÃO: Decodifica a chave Base64 para obter os bytes de tamanho correto
    ENCRYPTION_KEY = base64.b64decode(ENCRYPTION_KEY_B64)
except ImportError:
    # Fallback/Debug: Se o config.py falhar
    print("AVISO: Falha ao importar config. Usando chave de fallback.")
    ENCRYPTION_KEY = b'\xc9\xe6\xcf\xd3\x8fC\xfc\x7fr\xa2\xa9\x8f\xfd\x12\x04\x13\x17\xa5\xb2\x15\x1e\xb3\xd6\xae\x98\xe3\x0b\xa9\x04\x7a\x9e\x12'


def encrypt_data(data_to_encrypt: str) -> str:
    """Criptografa dados usando AES no modo CBC, gerando um IV aleatório."""
    # Instancia o cipher, o IV (Initialization Vector) é gerado automaticamente.
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_CBC)

    # Criptografa e empacota (pad) o dado.
    ct_bytes = cipher.encrypt(pad(data_to_encrypt.encode('utf-8'), AES.block_size))
    # O IV é prefixado ao ciphertext e codificado em Base64.
    encrypted_data = base64.b64encode(cipher.iv + ct_bytes).decode('utf-8')
    return encrypted_data

def decrypt_data(encrypted_data_base64: str) -> str:
    """Descriptografa dados de uma string Base64 (que contém IV e ciphertext)."""
    # Decodifica a string Base64 para bytes
    full_encrypted_bytes = base64.b64decode(encrypted_data_base64)

    # O IV é sempre o primeiro bloco (16 bytes para AES)
    iv = full_encrypted_bytes[:AES.block_size]
    ct_bytes = full_encrypted_bytes[AES.block_size:]

    # Cria o objeto cipher para descriptografia, usando o IV extraído
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_CBC, iv=iv)

    # Descriptografa e desempacota (unpad)
    decrypted_bytes = unpad(cipher.decrypt(ct_bytes), AES.block_size)

    return decrypted_bytes.decode('utf-8')