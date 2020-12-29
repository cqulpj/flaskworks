#coding=utf-8

import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
app.config['SECRET_KEY'] = 'dev'
# 在扩展类实例化前加载配置
db = SQLAlchemy(app)
# 实例化扩展类
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
# 创建用户加载回调函数，接受用户ID作为参数
def load_user(user_id):
    from watchlist.models import User
    user = User.query.get(int(user_id))
    return user

@app.context_processor          # 注册模板上下文处理函数
def inject_user():              # 函数名可以任意
    from watchlist.models import User
    users = User.query.all()
    return dict(user=users[-1]) # 需要返回字典，等同于{'user': user}

from watchlist import views, errors, commands

