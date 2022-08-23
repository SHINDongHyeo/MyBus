import configparser as parser

def getkey():
    properties = parser.ConfigParser()
    properties.read("./config.ini")
    app = properties["APP"]
    appkey = app["key"]
    return appkey