#coding=utf-8

from watchlist import db, app
from flask import Flask, render_template

@app.errorhandler(404)          # 传入要处理的错误代码
def page_not_found(e):          # 接收异常对象做为参数
    return render_template('404.html'), 404

