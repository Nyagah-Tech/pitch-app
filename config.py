class Config:
    '''
    general configuration of parent class
    '''

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dan:12345@localhost/pitch'
    pass

class ProdConfig (Config):
    '''
    this is production child class
    Args:
        Config:the parent configuration class with general configuration settings
    '''

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

    