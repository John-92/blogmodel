# -*- coding=utf-8 -*-
# @Time: 2022/8/27 23:13
# @Author: John
# @File: app.py
# @Software: PyCharm
from flask import Flask, render_template, request, redirect, url_for, abort, flash
# from jinja2 import escape


from markupsafe import escape
# template_folder指定模板的目录，static_folder指定静态文件的目录，static_url_path指定静态路径
# 通过flask routes可以查看路由信息
app = Flask(__name__,static_folder='static',static_url_path='/')

@app.before_first_request
def start_flask():
    print("start init")

@app.route("/")
def hello_world():
    name=request.args.get('name','Flask')
    name=request.args.get('name2','Flask')
    print(name)
    # return f'{name}'
    # return render_template("index-1.html")
    # return render_template("text.html")
    return render_template("post.html")

colors=['white','black','pink']
@app.route("/test/<any(%s):color>"% str(colors)[1:-1])
def test(color):
    name=request.args.get('name','Flask')
    name=request.args.get('name2','Flask')
    print(color)
    return f'{color}'
    # return render_template("index.html")

@app.route("/hello")
def hello():
    print(request.args.get('next'))
    return redirect(request.args.get('next'))

@app.route("/bar")
def ext():
    return '<h1>next page</h1><a href="%s">sss</a>' %url_for('hello_world',next=request.full_path)

@app.route("/xss")
def xss():
    name=request.args.get('name')
    return '<h1>next page %s</h1>' %escape(name)

@app.route("/flash")
def just_flash():
    flash("i am flash")
    return redirect(url_for('index'))
    # return '<h1>next page %s</h1>' %escape(name)

@app.route("/hi")
def hi():
    name=request.args.get('name','Flask')
    name=request.args.get('name2','Flask')
    print(name)
    return f'{name}'

@app.route("/jinja")
def jinja():
    #将变量渲染到模板上
    user={}
    user['username']='john'
    user['bio']='jinja test'
    movies=[
        {'name':'helloworld','year':'1998'},
        {'name':'helloworld2','year':'1999'},
        {'name':'helloworld3','year':'1997'},
        {'name':'helloworld4','year':'1996'}
    ]
    return render_template('jinja.html',user=user,movies=movies)

@app.route("/404")
def not_found():
    abort(404)
    return redirect(url_for('hello_world'))


if __name__ == '__main__':
    app.run(debug=True)
    app.secret_key='129-726-914'