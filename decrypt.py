import sys
import getpass
import cryptography
import gosh

password = gosh.cryptpass()
dec = cryptography.decrypt(sys.stdin.buffer.read(), password)
sys.stdout.buffer.write(dec)