import logging


class Logger(logging.getLoggerClass()):

    def __init__(self):
        super(Logger, self).__init__()

    def getLogger(self):
        """"""