import hashlib
inp = 'ckczppom'

i = 117946
while True:
    i += 1
    test = inp + str(i)
    hashed = hashlib.md5(test).hexdigest()
    if hashed[0:6] == '000000':
        print(i)
        break
