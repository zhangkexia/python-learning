# initial byte string
s = b'hello'

# encode as hex
import binascii
h = binascii.b2a_hex(s)
print(h)

# decode back to bytes
print(binascii.a2b_hex(h))


import base64
h = base64.b16encode(s)
print(h)
print(base64.b16decode(h))
