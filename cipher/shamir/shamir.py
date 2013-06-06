from pyssss.PySSSS import encode, decode
from StringIO import StringIO

def generate_secrets(S, n, k):
	assert n >= k and k > 0 and n > 0
	k += 1 # TODO: needs one more?!
	secrets = []
	for i in xrange(n):
		secrets.append(StringIO())

	encode(StringIO(S), secrets, k)
	return [x.getvalue().encode('hex') for x in secrets]

def recreate_secret(secrets):
	output = StringIO()
	inputs = [StringIO(secret.decode('hex')) for secret in secrets]
	decode(inputs, output)
	return output.getvalue()
