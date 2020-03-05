import logging
import datetime

today = datetime.datetime.today().strftime("%Y%m%d")

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    filename='./log/test_log_{}.log'.format(today),
                    filemode='a+')

tp = 0


def my_logger(func):
    def do_func(*args, **kw):
        global tp
        if tp == 0:
            logging.info(
                "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+- \n")
        tp += 1
        func_name = func.__name__
        logging.info("************** begin {0} **************".format(func_name))
        if args:
            logging.info("params list: {0}".format(list(args)))
        if kw:
            logging.info("other params: {0}".format(kw))
        res = func(*args, **kw)
        logging.info("result: {0}".format(res))
        return res

    return do_func
