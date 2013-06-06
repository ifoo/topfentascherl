from Crypto.PublicKey import RSA
from Crypto import Random


def generate_key(size=2048):
	return RSA.generate(size, Random.new().read)