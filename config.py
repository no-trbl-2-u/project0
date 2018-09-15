from tempfile import mkdtemp

ENV = 'development'
DEBUG = True
uri = 'postgres://postgres:11986143@127.0.0.1:5432/project0'
SQLALCHEMY_DATABASE_URI = uri
SECRET_KEY = 'Thisisasecret!'
SQLALCHEMY_TRACK_MODIFICATIONS = True
TEMPLATES_AUTO_RELOAD = True
SESSION_PERMANENT = False
SQLALCHEMY_ECHO = True

# Configure session to use filesystem (instead of signed cookies)
SESSION_FILE_DIR = mkdtemp()
SESSION_PERMANENT = False
SESSION_TYPE = "filesystem"
