import sys
import getpass
import cryptography
import gosh

password = gosh.cryptpass()
enc = cryptography.encrypt(sys.stdin.buffer.read(), password)
sys.stdout.buffer.write(enc)