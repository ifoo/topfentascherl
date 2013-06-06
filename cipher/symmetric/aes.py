from Crypto import Random
from Crypto.Cipher import AES
from hashlib import sha256

from ..utils.padding import pad, unpad

def encrypt(data, key, mode=AES.MODE_CBC):
	data = pad(data, AES.block_size)
	iv = Random.new().read(AES.block_size)
	cipher = AES.new(sha256(key).digest(), mode, iv)
	return iv + cipher.encrypt(data)

def decrypt(data, key, mode=AES.MODE_CBC):
	iv = data[:AES.block_size]
	cipher = AES.new(sha256(key).digest(), mode, iv)
	return unpad(cipher.decrypt(data[AES.block_size:]))
