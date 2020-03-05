import pymysql
import contextlib
from base.ConfBase import ConfBase
from base.MyLogger import my_logger

config = ConfBase.config


def to_strings(strings):
    return '"' + str(strings) + '"'


class SqlTools(object):

    # 初始化数据
    def __init__(self):
        config.read(ConfBase.config_file)
        self.__host = config.get('sql_config', 'host')
        self.__port = int(config.get('sql_config', 'port'))
        self.__user = config.get('sql_config', 'user')
        self.__passwd = config.get('sql_config', 'passwd')

    # 建立mysql链接上下文
    @contextlib.contextmanager
    def __connect_db(self):
        connect = pymysql.Connect(
            host=self.__host,
            port=self.__port,
            user=self.__user,
            passwd=self.__passwd,
            charset='utf8'
        )
        cursor = connect.cursor()
        try:
            yield cursor
        finally:
            connect.commit()
            cursor.close()
            connect.close()

    # 返回查询结果
    @my_logger
    def get_data(self, sql):
        res = []
        with self.__connect_db() as cursor:
            cursor.execute(sql)
            collection = cursor.fetchall()
            length = len(collection)
            if length == 1:
                return collection[0]
            elif length > 1:
                for row in collection:
                    res.append(row)
            else:
                pass
        return res
