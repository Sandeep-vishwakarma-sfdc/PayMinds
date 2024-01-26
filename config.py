
class Config(object):
    SECRET_KEY = 'test'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@127.0.0.1:3306/payminds'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://Sandeepsfdc:root%40123@Sandeepsfdc.mysql.pythonanywhere-services.com/payminds'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO=True
    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # ADMINS = ['your-email@example.com']
    # LANGUAGES = ['en', 'es']
    # MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    # POSTS_PER_PAGE = 25