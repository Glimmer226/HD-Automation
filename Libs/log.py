# encoding=utf-8
import logging
import logging.handlers
import os
import time


class Logging:
    def __dir(self):
        os.chdir("..")
        dirs = os.listdir(os.getcwd())
        self.path = os.getcwd() + "\\" + "logs"
        if "logs" in dirs:
            pass
        else:
            os.mkdir(self.path)

    def __logging(self):
        self.__logger_name = 'HD_automation'

        self.__postfix = "logs" + "_" + time.strftime("%Y%m%d", time.localtime()) + ".log"
        self.__logfile = os.path.join(self.path, self.__postfix)

        self.__logger = logging.getLogger('HD_automation')
        self.__logger.setLevel(logging.DEBUG)

        self.__handler = logging.handlers.RotatingFileHandler(self.__logfile, "a",
                                                              maxBytes=10240, backupCount=10,
                                                              encoding='utf-8')
        self.__handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%H:%S")

        self.__handler.setFormatter(formatter)
        self.__console = logging.StreamHandler()
        self.__console.setLevel(logging.DEBUG)
        self.__console.setFormatter(formatter)

        self.__logger.addHandler(self.__handler)
        self.__logger.addHandler(self.__console)

    def __init__(self):
        self.__dir()
        self.__logging()

    def debug(self, message):
        self.__logger.debug("%s" % message)

    def info(self, message):
        self.__logger.info("%s" % message)

    def warn(self, message):
        self.__logger.warning("%s" % message)

    def error(self, message):
        self.__logger.error("%s" % message)


log = Logging()

if __name__ == "__main__":
    log.info("info message")
    log.warn("warn message")
    log.error("error message")



