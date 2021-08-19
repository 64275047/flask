from flask import Flask, request


app = Flask(__name__)


@app.route('/register/', methods=['GET', 'POST'])  # method指定请求方式
def register():
    print(request.form)     # 获取form表单提交过来的非文件数据,类似字典
    for item in request.form:
        print(item)
    avatar_obj = request.files.get('avatar')  #获取文件，类似字典
    avatar_obj.save(avatar_obj.name)    # 保存文件，保存到当前py文件所在路径下
    return '注册成功'




if __name__ == '__main__':
    app.run()