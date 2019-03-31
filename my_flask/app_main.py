from flask import Flask,render_template,url_for,request,make_response,redirect
from Myhelp import Myhelp_a
app = Flask(__name__)  #创建一个Flask对象


# @app.route('/')#相当于url路径
# def hello_world():
#     #请求方式
#     print(request.method)
#     print(request.args.get('name'))
#     # print(url_for('user',n='admin',_external=True))#方法名    打印出对应的@app.route('')
#
#     return 'Hello World!'
#
@app.route('/index')
def index():
    # request.cookies.get('username')
    return render_template('index.html')
@app.route('/login',methods=['POST','GET'])   #既可以接收post 也可以  get
def login():
    name = request.form['username']
    password = request.form['password']
    print(name)
    if name == 'czq' and password == 'pp507':
        resp = make_response(render_template('index.html'))
        resp.set_cookie('username', 'admin')
        # return redirect(url_for('user'))   #  重定向   如果当前方法不行  重新发送到 url_for   里面的方法里
        return resp
    else:
        return  render_template('b.html')
class obj():
    name = ''
    age = ''
@app.route('/user/<n>')
def user(n):
    object = obj()
    object.name = '啥班级'
    object.age = 18
    # dict1 = {'name':n,'age':18}
    # list1 = [n,123,'杀杀杀']
    return render_template('user.html',name=object)
@app.route('/user/<n>')
def user(n):
    list1 = [1,2,3,65,78]
    list2 = [4,5,6,77,99]
    return render_template ('user.html',name=list1,name2 = list2)

@app.route('/a')
def a():
    return render_template('a.html')

@app.route('/b')
def b():
    if request.cookies.get('username'):
        return render_template('b.html')
    else:
        return render_template('index.html')

@app.route('/abc',methods=['POST'])
def index1():
    username = request.form['username']
    password = request.form['password']
    print(username)
    h = Myhelp_a()
    sql = 'select * from card1_zhuce_card where name = %s and password = %s'
    params = [username,password]
    result = h.queryone(sql,params)
    print(result)
    if result:
        # 设置cookie
        resp = make_response(render_template('a.html'))
        resp.set_cookie('username', 'use')
        return resp
    else:
        return render_template('b.html')


if __name__ == '__main__':
    app.run()  #启动服务
