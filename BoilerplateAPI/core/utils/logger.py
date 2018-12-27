import logging
import logging.handlers
import os

from BoilerplateAPI import config


def get_logger(name):
	"""

	:param name:
	:return:
	"""
	# create logger
	# logger = logging.basicConfig(filename=config.LOG_DIR, filemode='w', level=logging.DEBUG)
	logger = logging.getLogger(name)
	if not os.path.isdir(config.LOG_DIR):
		os.makedirs(config.LOG_DIR)

	# create console handler and set level to debug
	handler = logging.TimedRotatingFileHandler(config.LOG_DIR + name, encoding="bz2", when="midnight")
	handler.setLevel(logging.DEBUG)

	# create formatter
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

	# add formatter to ch
	handler.setFormatter(formatter)

	# add ch to logger
	logger.addHandler(handler)

	return logger
