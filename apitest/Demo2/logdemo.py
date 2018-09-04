# coding: utf-8

import logging, time, os

# if __name__ == '__main':
#     logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s [line: %(lineno)d] %(levelname)s %(message)s', datefmt='%a, %d %b %Y %H:%M:%S', filemode='w')
#     console = logging.StreamHandler()
#     console.setLevel(logging.INFO)
#     formatter = logging.Formatter('%(name)-12 s: %(levelname)-8 s %(message)s')
#     console.setFormatter(formatter)
#     logging.getLogger('').addHandler(console)
#     logging.debug(u'这是bug级别日志记录')
#     logging.info(u'这是提示信息级别日志记录')
#     logging.warning(u'这是警告级别日志记录')
log_path = 'D:\\test\\newp\\report'
class Log:
    def __init__(self):
        self.logname = os.path.join(log_path, '%s.log'%time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
        def __console(self, level, message):
            fh = logging.FileHandler(self.logname, 'a')
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(self.formatter)
            self.logger.addHandler(fh)
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)
            ch.setFormatter(self.formatter)
            self.logger.addHandler(ch)
            if level == 'info':
                self.logger.info(message)
            elif level == 'debug':
                self.logger.debug(message)
            elif level == 'warning':
                self.logger.warning(message)
            elif level == 'error':
                self.logger.error(message)
            self.logger.removeHandler(ch)
            self.logger.removeHandler(fh)
            fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

if __name__ == '__main__':
    log = Log()
    log.info('——测试开始——')
    log.info('输入密码')
    log.warning('——测试结束——')