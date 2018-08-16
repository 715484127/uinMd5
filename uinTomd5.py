import hashlib
from threading import Thread
import time
import pymysql
from multiprocessing import Process


def batch1(uinstart1, uinend1):
    time_start = time.time()  # time.time()为1970.1.1到当前时间的毫秒数
    db = pymysql.connect("localhost", "root", "2006wang", "uin")
    cursor = db.cursor()
    cursor.execute('use uin')
    md5str = hashlib.md5()
    count = 1
    while True:
        uin = 'mm' + str(uinstart1)
        md5str.update(uin.encode(encoding='utf-8'))
        md5insert = md5str.hexdigest()
        print("第%d条MD5：%s" % (count, md5insert))
        sql = """insert into `00` VALUES ('%s',%d)""" % (md5insert, uinstart1)
        # noinspection PyBroadException
        try:
            # 执行sql语句
            cursor.execute(sql)

        except BaseException:
            # 发生错误时回滚
            db.rollback()

        if uinstart1 == uinend1:
            break
        uinstart1 += 1
        count += 1
    # 执行sql语句
    db.commit()
    time_end = time.time()
    print(time_end - time_start)


if __name__ == '__main__':
    # t1 = Thread(target=batch1, name='batch1', args=(100000000, 102000000))
    # t2 = Thread(target=batch1, name='batch2', args=(102000001, 104000001))
    # t3 = Thread(target=batch1, name='batch3', args=(104000002, 106000002))
    # t4 = Thread(target=batch1, name='batch4', args=(106000003, 108000003))
    # t5 = Thread(target=batch1, name='batch5', args=(108000004, 110000004))
    # t6 = Thread(target=batch1, name='batch6', args=(110000005, 112000005))
    # t7 = Thread(target=batch1, name='batch7', args=(112000006, 114000006))
    # t8 = Thread(target=batch1, name='batch8', args=(114000007, 116000007))
    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
    # t5.start()
    # t6.start()
    # t7.start()
    # t8.start()
    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    # t5.join()
    # t6.join()
    # t7.join()
    # t8.join()

    p1 = Process(target=batch1, args=(100000000, 102000000))
    p2 = Process(target=batch1, args=(102000001, 104000001))
    p3 = Process(target=batch1, args=(104000002, 106000002))
    p4 = Process(target=batch1, args=(106000003, 108000003))
    p5 = Process(target=batch1, args=(108000004, 110000004))
    p6 = Process(target=batch1, args=(110000005, 112000005))
    p7 = Process(target=batch1, args=(112000006, 114000006))
    p8 = Process(target=batch1, args=(114000007, 116000007))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()

    print('主线程开始执行......')
