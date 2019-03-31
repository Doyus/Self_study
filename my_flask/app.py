from flask import Flask,render_template,url_for,request,make_response,redirect
from MyHelper import MyHelper
from flask import Flask

hel = MyHelper('127.0.0.1','root','x5','mytest')
app = Flask(__name__)

#注意commit提交

@app.route('/',methods=['POST','GET'])


def hello_world():

    return render_template('d_login.html')


@app.route('/ver',methods=['POST','GET'])
def yanzheng():
    name = request.form['username']
    password = request.form['password']
    password = int(password.strip())
    # print('用户名密码')
    # print(name,password)
    # print('用户名密码')
    sql = 'select name,pwd from ming where name="%s" and pwd="%d"'%(name,password)
    res = hel.queryAll(sql)
    if(res):
       # if result:
       #  # 设置cookie
       #  # resp = make_response(render_template('s_list.html'))
       #  # resp.set_cookie('username', 'dongyupeng')
       #  # return resp
        return render_template('zhongjian.html')
    else:
        return '<h1>用户名或者密码输入错误</h1>'
    # return redirect('http://localhost:5000/')

@app.route('/main',methods=['POST','GET'])

def main():
    sql = 'select * from ming'
    res = hel.queryAll(sql)
    list1 = []
    # print('结果')
    # print(res)
    # print('结果')
    for var in res:
        print(var)
        dic = {}

        dic['name']   = str(var[1])
        dic['age']   = str(var[2])
        dic['id']   = str(var[0])
        list1.append(dic)
    return render_template('s_list.html',N=list1)


@app.route('/delete',methods=['POST','GET'])

def delete():
    id1 = int(request.args.get('idd'))
    print('asdfffffffffffffffffffffffffffffffffffffffff')
    # print(id1)
    sql = 'delete from ming where id="%d"'%(id1)
    print(sql)
    res = hel.exe(sql)
    print(res)
    return redirect('http://localhost:5000/main')

@app.route('/reg',methods=['POST','GET'])

def reg():

    return render_template('s_register.html')

@app.route('/register',methods=['POST','GET'])

def register():
    name = request.form['name']
    password = int(request.form['pwd'])
    age = int(request.form['age'])
    sql = 'insert into ming(name,age,pwd) values(%s,%d,%d)'%(name,password,age)
    print('sql操作语句')
    print(sql)
    print('sql操作语句')
    res = hel.exe(sql)
    return render_template('zhongjian1.html')

@app.route('/update',methods=['POST','GET'])

def update():
    id1 = int(request.args.get('idd'))
    sql = 'select * from ming where id="%d"'%(id1)
    res = hel.queryAll(sql)
    list1 = []
    # print('结果')
    # print(res)
    # print('结果')
    for var in res:
        print(var)
        dic = {}

        dic['name']   = str(var[1])
        dic['age']   = str(var[2])
        dic['id']   = str(var[0])
        list1.append(dic)
    hel.close()
    return render_template('s_update.html',N=list1)

@app.route('/update1',methods=['POST','GET'])

def update1():
    id1 = int(request.form['id'])
    name = request.form['name']
    age = int(request.form['age'])
    sql = 'update ming set id="%d",name="%s",age="%d" where id="%d"'%(id1,name,age,id1)
    res = hel.exe(sql)
    return redirect('http://localhost:5000/main')


















if __name__ == '__main__':

    app.run(debug=True)

























































'''

第4行，引入Flask类，Flask类实现了一个WSGI应用

第5行，app是Flask的实例，它接收包或者模块的名字作为参数，但一般都是传递__name__。

    让flask.helpers.get_root_path函数通过传入这个名字确定程序的根目录，以便获得静态文件和模板文件的目录。

第7~9行，使用app.route装饰器会将URL和执行的视图函数的关系保存到app.url_map属性上。

    处理URL和视图函数的关系的程序就是路由，这里的视图函数就是hello_world。

第11行，使用这个判断可以保证当其他文件引用这个文件的时候（例如“from hello import app”）不会执行这个判断内的代码，也就是不会执行app.run函数。

第12行，执行app.run就可以启动服务了。默认Flask只监听虚拟机的本地127.0.0.1这个地址，端口为5000。

    而我们对虚拟机做的端口转发端口是9000，所以需要制定host和port参数，0.0.0.0表示监听所有地址，这样就可以在本机访问了。

    服务器启动后，会调用werkzeug.serving.run_simple进入轮询，默认使用单进程单线程的werkzeug.serving.BaseWSGIServer处理请求，

    实际上还是使用标准库BaseHTTPServer.HTTPServer，通过select.select做0.5秒的“while TRUE”的事件轮询。

    当我们访问“http://127.0.0.1:9000/”,通过app.url_map找到注册的“/”这个URL模式,就找到了对应的hello_world函数执行，返回“hello world!”,状态码为200。

    如果访问一个不存在的路径，如访问“http://127.0.0.1:9000/a”,Flask找不到对应的模式，就会向浏览器返回“Not Found”，状态码为404

'''
