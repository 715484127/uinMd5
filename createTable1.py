
import pymysql


if __name__ == '__main__':
    print('主线程开始执行......')
    db = pymysql.connect("localhost", "root", "2006wang", "uin")
    cursor = db.cursor()

    for data in range(0, 80):
        if data <= 9:
            data = '0' + str(data)
        tableName = str(data)
        print('开始创建表: %s' % tableName)
        sql = """CREATE TABLE `""" + tableName + """` (
                 `md5` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
                 `uin` varchar(13) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
                 PRIMARY KEY (`md5`) USING BTREE )
                 ENGINE = MyISAM CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact"""
        cursor.execute(sql)

    db.close()




