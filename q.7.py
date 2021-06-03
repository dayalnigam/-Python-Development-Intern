import logging

logger = logging.getLogger('2227 2227 D')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('mylog.log')
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)


logger.addHandler(ch)
logger.addHandler(fh)


logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')