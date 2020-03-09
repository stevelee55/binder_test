from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

encrpyted_text = "gAAAAABeZbuxy54OPTpgxqRmI7VoJHdN5x5KRiudF8a50H6w-8KZQxJ4vNmoLKBsEO5443wB1HKrOHZsf0aFpa2kxdjeH4PxeMol7v2sWA8rAS552CLWvuNCkowkOb3LVqVsNVBxcDiJzEIEgmPi8HLA43L201HRUA=="

def getKey(password):
	password_provided = password # This is input in the form of a string
	password = password_provided.encode() # Convert to type bytes
	salt = b'_salt' # bytes(os.urandom(16))
	kdf = PBKDF2HMAC(
	    algorithm=hashes.SHA256(),
	    length=32,
	    salt=salt,
	    iterations=100000,
	    backend=default_backend()
	)
	key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once
	return key

def decrypt(key):
	fernet = Fernet(key)
	decrypted = fernet.decrypt(bytes(encrpyted_text.encode()))
	text_decrypted = decrypted.decode("utf-8")
	creds = text_decrypted.split("&")
	return creds[0], creds[1]

def getCreds(password):
	key = getKey(password)
	creds_0, creds_1 = decrypt(key)
	return creds_0, creds_1
