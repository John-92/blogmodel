# -*- coding=utf-8 -*-
# @Time: 2022/8/27 23:13
# @Author: John
# @File: app.py
# @Software: PyCharm
from flask import Flask, render_template, request, redirect, url_for, abort
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
    return render_template("index.html")

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
    # name=request.args.get('name','Flask')
    # name=request.args.get('name2','Flask')
    # print(name)
    # return f'{name}'
    # return '',302,{'Location','www.baidu.com'}
    # return redirect(request.referrer or url_for('hello_world'))
    print(request.args.get('next'))
    return redirect(request.args.get('next'))

@app.route("/bar")
def ext():
    return '<h1>next page</h1><a href="%s">sss</a>' %url_for('hello_world',next=request.full_path)
    # print("hhh")
    # return 'hhh'

@app.route("/xss")
def xss():
    name=request.args.get('name')
    return '<h1>next page %s</h1>' %escape(name)

@app.route("/hi")
def hi():
    name=request.args.get('name','Flask')
    name=request.args.get('name2','Flask')
    print(name)
    return f'{name}'



@app.route("/404")
def not_found():
    abort(404)
    return redirect(url_for('hello_world'))


if __name__ == '__main__':
    app.run(debug=True)