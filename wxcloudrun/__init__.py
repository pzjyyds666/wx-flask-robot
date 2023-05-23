from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
import config

# 因MySQLDB不支持Python3，使用pymysql扩展库代替MySQLDB库
pymysql.install_as_MySQLdb()

# 初始化web应用
app = Flask(__name__, instance_relative_config=True)
app.config['DEBUG'] = config.DEBUG

from werobot.contrib.flask import make_view #使用make_view依赖到flask项目
from wxcloudrun import robot
app.add_url_rule(rule='/api/app/',        # WeRoBot挂载地址
                 endpoint='werobot',             # Flask的endpoint
                 view_func=make_view(robot),#robot是robot文件
                 methods=['GET', 'POST'])

# 设定数据库链接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/flask_demo'.format(config.username, config.password,
                                                                             config.db_address)

# 初始化DB操作对象
db = SQLAlchemy(app)

# 加载控制器
from wxcloudrun import views

# 加载配置
app.config.from_object('config')
