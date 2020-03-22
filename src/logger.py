import logging


class Logger:

    def __init__(self):
        self._logger = logging.getLogger('Rest_Service_Log')
        self._logger.setLevel(logging.DEBUG)
        self._fh = logging.FileHandler('%(asctime)s_debug.log')
        self._fh.setLevel(logging.DEBUG)
        self._logger.addHandler(self._fh)
        self._formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self._fh.setFormatter(self._formatter)
        self._logger.addHandler(self._fh)

    def log_info(self, message):
        self.logger.debug('Debug-Nachricht')
        self.logger.info(message)
        self.logger.warning('Warnhinweis')
        self.logger.error('Fehlermeldung')
        self.logger.critical('Schwerer Fehler')