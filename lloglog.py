import logging

logger = logging.getLogger(__name__)

logger.setLevel(level=logging.INFO)
formatter = logging.Formatter(fmt='%(asctime)s--%(name)s--%(levername)s--%(message)s', datefmt='%Y-%m-%D %H:%M:%S')
file_handler = logging.FileHandler('outlog.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.info('Start:')
logger.warning('Something error will occur')
try:
    result = 10 / 0
except Exception as e:
    logger.exception('error')
#    logger.error('fail to get result',exc_info=True)
logger.info('finished')
