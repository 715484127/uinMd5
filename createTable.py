from itertools import permutations
import pymysql


if __name__ == '__main__':
    print('主线程开始执行......')
    db = pymysql.connect("localhost", "root", "2006wang", "uin")
    cursor = db.cursor()

    tableNameList = list(permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'], 2))
    tableNameList.append(('0', '0'))
    tableNameList.append(('1', '1'))
    tableNameList.append(('2', '2'))
    tableNameList.append(('3', '3'))
    tableNameList.append(('4', '4'))
    tableNameList.append(('5', '5'))
    tableNameList.append(('6', '6'))
    tableNameList.append(('7', '7'))
    tableNameList.append(('8', '8'))
    tableNameList.append(('9', '9'))
    tableNameList.append(('a', 'a'))
    tableNameList.append(('b', 'b'))
    tableNameList.append(('c', 'c'))
    tableNameList.append(('d', 'd'))
    tableNameList.append(('e', 'e'))
    tableNameList.append(('f', 'f'))

    for data in tableNameList:
        tableName = data[0] + data[1]
        print('开始创建表: %s' % tableName)
        sql = """CREATE TABLE `""" + tableName + """` (
                 `md5` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
                 `uin` varchar(13) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
                 PRIMARY KEY (`md5`) USING BTREE )
                 ENGINE = MyISAM CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact"""
        cursor.execute(sql)

    db.close()




