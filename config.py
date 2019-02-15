# -*- coding: utf-8 -*-

import os
import sys
if sys.version_info > (2, 7):
    import ConfigParser as CP
else:
    import configparser as CP


BRAND_NAME = 'Falcon REST API Template'
VERSION = '0.0.1'

APP_ENV = os.environ.get('APP_ENV') or 'local'  # or 'live' to load live
INI_FILE = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'conf/{}.ini'.format(APP_ENV))

CONFIG = CP.ConfigParser()
CONFIG.read(INI_FILE)

DATABASE_URL = CONFIG.get('database', 'name')

LOG_LEVEL = CONFIG.get('logging', 'level')
