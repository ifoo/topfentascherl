

def pad(data, block_size):
	return data + (block_size - len(data) % block_size) * chr(block_size - len(data) % block_size)

def unpad(data):
	return data[0:-ord(data[-1])]