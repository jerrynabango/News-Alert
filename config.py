import os

class Config:
    '''
    General configuration parent class
    '''
    
    SOURCES_BASE_URL ='https://newsapi.org/v2/sources?apiKey='
    
    ARTICLES_BASE_URL = 'http://newsapi.org/v2/everything?q=bitcoin&from=2020-04-30&sortBy=publishedAt&apiKey=API_KEY'
    
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY ')
    
    @staticmethod
    def init_app(app):
        pass

    



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}