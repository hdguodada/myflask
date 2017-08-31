import os 
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    '基类，定义基本配置'
    SECRET_KEY = 'hard to guess'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[FLASY]' # 主题前面加的修饰前缀
    FLASKY_MAIL_SENDER = 'FLASKY Admin <18358928574@sina.cn>' # <> 前面的是昵称， <>里的是发件人
    FLASKY_ADMIN = '18358928574@sina.cn' # 指管理员是谁
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    '开发环境库'
    DEBUG = True
    MAIL_SERVER = 'smtp.sina.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = '18358928574@sina.cn'
    MAIL_PASSWORD = 'ajian2013'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:passwd@localhost/myflask'


class TestingConfig(Config):
    '测试环境库'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:passwd@localhost/myflask'


class ProductConfig(Config):
    '生产环境库'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:passwd@localhost/myflask'


'注册不同的环境和一个默认配置'
config = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'pruduction': ProductConfig,
        'default': DevelopmentConfig
        }
