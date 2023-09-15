
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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"

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}

## Enter your Open API Key here
OPENAI_API_KEY = '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'
# OPENAI_API_KEY = 'ssk-qxaJBfbSPqghSYTwFcJ5T3BlbkFJjezOLvuKz87JJrlQmqK8'
