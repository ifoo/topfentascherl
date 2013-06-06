from cipher.symmetric.aes import encrypt, decrypt


D = 'hello world'
K = 'foo bar'

enc = encrypt(D, K)
dec = decrypt(enc, K)

print dec