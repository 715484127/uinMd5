from flask import Flask, abort, request, jsonify
import pymysql
import time
import logging


# 配置日志
logname = "uin.log"
filehandler = logging.FileHandler(filename=logname, encoding="utf-8")
fmter = logging.Formatter(
    fmt="%(asctime)s.%(msecs)03d %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")
filehandler.setFormatter(fmter)
loger = logging.getLogger(__name__)
loger.addHandler(filehandler)
loger.setLevel(logging.INFO)


app = Flask(__name__)

# 测试数据暂时存放
tasks = []


@app.route('/add_task/', methods=['POST'])
def add_task():
    if not request.json or 'id' not in request.json or 'info' not in request.json:
        abort(400)
    task = {
        'id': request.json['id'],
        'info': request.json['info']
    }
    tasks.append(task)
    return jsonify({'result': 'success'})


@app.route('/get_task/', methods=['GET'])
def get_task():
    if not request.args or 'id' not in request.args:
        # 没有指定id则返回全部
        return jsonify(tasks)
    else:
        task_id = request.args['id']
        task = filter(lambda t: t['id'] == int(task_id), tasks)
        return jsonify(task) if task else jsonify({'result': 'not found'})


# 根据MD5值获取uin
@app.route('/get_uin', methods=['GET'])
def get_uin():
    time_start = time.time()
    if not request.args or 'md5' not in request.args:
        abort(400)
    else:
        result = ()
        result_json = {'uin': 'not found'}
        md5 = request.args['md5'].upper()
        loger.info("|#请求参数|#MD5=" + md5)
        if not md5:
            loger.info("|#请求参数|#MD5=" + md5 + "|#请求参数错误")
        else:
            db = pymysql.connect("localhost", "root", "2006wang", "uin")
            cursor = db.cursor()
            for data in range(0, 80):
                if data <= 9:
                    data = '0' + str(data)
                table_name = str(data)
                sql = """select uin from `""" + table_name + \
                      """` where md5 =  '""" + md5 + """'"""
                cursor.execute(sql)
                result = cursor.fetchone()
                if not result:
                    loger.info(
                        "|#table_name:" +
                        table_name +
                        "|#MD5:" +
                        md5 +
                        "|#没有对应的UIN")
                else:
                    loger.info(
                        "|#table_name:" +
                        table_name +
                        "|#MD5:" +
                        md5 +
                        "|#UIN:" +
                        result[0])
                    break
        time_end = time.time()
        if not result:
            result = ()
            loger.info("|#查询总耗时:%.2f秒|#MD5=%s|#UIN=%s|#没有查询到UIN" % ((time_end - time_start), md5, ''))
        else:
            result_json.update(uin=result[0])
            loger.info("|#查询总耗时:%.2f秒|#MD5=%s|#UIN=%s" % ((time_end - time_start), md5, result[0]))

        return jsonify(result_json) if result else jsonify({'uin': 'not found'})


if __name__ == "__main__":
    loger.info("|#根据MD5获取UIN服务开始启动......")
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.run(host="0.0.0.0", port=9000, debug=False)
