from flask import Flask, render_template
import pymysql

app = Flask(__name__)

conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='Youyuan123.',
    db='student',
    charset='utf8'
)


@app.route('/')
def hello_world():
    cur = conn.cursor()

    # get annual sales rank
    sql = "select * from student"
    cur.execute(sql)
    content = cur.fetchall()

	# 获取表头
    sql = "SHOW FIELDS FROM student"
    cur.execute(sql)
    labels = cur.fetchall()
    labels = [l[0] for l in labels]

    return render_template('/mysql/index.html', labels=labels, content=content)


if __name__ == '__main__':
    #app.run()
    app.run(host='172.18.8.58',port=8080)
