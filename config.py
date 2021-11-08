import os

class Config:

    SECRET_KEY='SECRET_KEY'
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://geroge:kamakia91@localhost/pitchh'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

   
  

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
    # connecting to database

    DEBUG = True

    #connecting to Gmail
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Pitchh'
    SENDER_EMAIL = 'george.macharia@student.moringaschool.com'

  # editor


  

config_options = {
'development':DevConfig,
'production':ProdConfig,
}
