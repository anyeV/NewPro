import time


class Printer(object):

    def __init__(self, lv=0, write_file=None):
        self.ctl = lv
        self.write_file = write_file

    def __my_print(self, strings, set_level):

        if self.ctl != 0:
            pri_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            if set_level >= self.ctl:
                strs = pri_time + " LOG_INFO  " + strings
                print("\033[0;32;0m" + strs + " \033[0m")
            else:
                return
        else:
            return

    def my_print_debug(self, strings):
        self.__my_print(strings, 1)

    def my_print_info(self, strings):
        self.__my_print(strings, 2)

    def my_print_error(self, strings):
        self.__my_print(strings, 3)
