from BoilerplateAPI.core.utils.logger import get_logger


class DummyHandler:

	def __init__(self):
		self.logger = get_logger('Dummy')

	def test_logger(self):
		"""

		:return:
		"""
		self.logger.info('This is the logger test.')
		return {'status': True}
