# -*- coding: utf-8 -*-

import sys
import logging

import config


logging.basicConfig(level=config.LOG_LEVEL)
LOG = logging.getLogger('API')
LOG.propagate = False

INFO_FORMAT = '[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s'
DEBUG_FORMAT = '[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s [in %(pathname)s:%(lineno)d]'
TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S %z'


def file_log():
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('log/app.log', 'a', 1 * 1024 * 1024, 10)
    formatter = logging.Formatter(INFO_FORMAT, TIMESTAMP_FORMAT)
    file_handler.setFormatter(formatter)
    LOG.addHandler(file_handler)


def stdout_log():
    stream_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(DEBUG_FORMAT, TIMESTAMP_FORMAT)
    stream_handler.setFormatter(formatter)
    LOG.addHandler(stream_handler)


if config.APP_ENV == 'live':
    file_log()

if config.APP_ENV == 'dev' or config.APP_ENV == 'local':
    file_log()
    stdout_log()


def get_logger():
    return LOG
