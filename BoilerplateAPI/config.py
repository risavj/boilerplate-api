import os


from ast import literal_eval

import configparser as configparser

config_parser = configparser.RawConfigParser()
config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.conf')
print(config_file)
config_parser.read(open(config_file))

BASE_DIR = os.getcwd()
LOG_DIR = os.path.join(os.getcwd(), 'logs/')

settings =
api_settings = literal_eval(config_parser.get('DEFAULT', 'api_settings', raw=False))
