import logging


class Logger:

    def __init__(self, name):
        self._logger = logging.getLogger(name)
        self._logger.setLevel(logging.DEBUG)
        self._fh = logging.FileHandler('debug.log')
        self._fh.setLevel(logging.DEBUG)
        self._logger.addHandler(self._fh)
        self._formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self._fh.setFormatter(self._formatter)
        self._logger.addHandler(self._fh)

    def log_info(self, message):
        self._logger.info(message)

    def log_debug(self, message):
        self._logger.debug(message)

    def log_warning(self, message):
        self._logger.warning(message)

    def log_error(self, message):
        self._logger.error(message)

    def log_critical(self, message):
        self._logger.critical(message)
