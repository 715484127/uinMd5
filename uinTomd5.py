import hashlib
from threading import Thread
import time
from itertools import combinations, permutations


def batch1(name):
    time_start = time.time()  # time.time()为1970.1.1到当前时间的毫秒数
    uinstart1 = 100000000
    uinend1 = 500000000
    # uinend1 = 2000000000
    md5str = hashlib.md5()

    while True:
        uin = str(uinstart1)
        md5str.update(uin.encode(encoding='utf-8'))
        print(md5str.hexdigest())
        if uinstart1 == uinend1:
            break
        uinstart1 += 1

    time_end = time.time()
    print(time_end - time_start)


if __name__ == '__main__':
    # t = Thread(target=batch1, args=('1-5',))
    # t.start()
    print('主线程')
    print(list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f'], 2)))

