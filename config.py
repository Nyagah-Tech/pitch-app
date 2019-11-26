import os

class Config:
    '''
    general configuration of parent class
    '''
    SECRET_KEY ='dm/01254'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dan:12345@localhost/pitch'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #email configuration
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME ='danmuv12@gmail.com'
    MAIL_PASSWORD ='Dm17/01254'


    pass

class ProdConfig (Config):
    '''
    this is production child class
    Args:
        Config:the parent configuration class with general configuration settings
    '''
     SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig (Config):
    '''
    prduction configuration child class

    Args:
        Config:parent configuration class with general configuration setting
    '''
    pass 

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}

    