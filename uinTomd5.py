import hashlib

uinStart1 = 100000000
uinEnd1 = 2000000000
md5Str = hashlib.md5()

while True:
    uin = str(uinStart1)
    md5Str.update(uin.encode(encoding='utf-8'))
    print(md5Str.hexdigest())
    if uinStart1 == uinEnd1:
        break
    uinStart1 += 1




