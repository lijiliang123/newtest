import logging

'''
basicConfig方法，进行日志文件的基本配置，如
leverl日志级别（INFO/DEBUG），format格式化，
日志文件写入方式filemode（w－后写入, a－清除追加写入）,
日志文件名称filename，

'''

# 日志文件基本配置：
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s--%(name)s--%(levelname)s--%(message)s',
                    filemode='a',
                    filename='log.txt')
# 日志对象初始化：
logger = logging.getLogger(__name__)

logger.info('This is a log info')
logger.debug('This is DEBUGGING')
logger.warning('This is WARNING')
logger.info('LOG FINISHED')

with open('log.txt', 'r') as f:
    while True:
        s = f.readline()
        if len(s) == 0:
            break
        else:
            print(s)

#  s=f.read()
#  print(s)
