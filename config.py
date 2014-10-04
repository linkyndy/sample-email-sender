import os

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
MONGO_URI = os.environ['MONGOLAB_URI']
SENDGRID_USERNAME = os.environ['SENDGRID_USERNAME']
SENDGRID_PASSWORD = os.environ['SENDGRID_PASSWORD']
DEFAULT_FROM_EMAIL = 'sample-email-sender@example.com'
DEBUG = os.environ['DEBUG']
