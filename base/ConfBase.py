import configparser


class ConfBase:
    config = configparser.ConfigParser()
    config_file = "./base/config.ini"

    @classmethod
    def pro_save_params(cls, func):
        def _get_params(*args, **params):
            if params:
                cls().config.read(cls().config_file)
                for key in params.keys():
                    cls().config.set("oil", str(key), str(params[key]))
                    cls().config.write(open(cls().config_file, 'w'))
            res = func(*args, **params)
            return res

        return _get_params

    @classmethod
    def to_stings(cls, strings):
        return '"' + str(strings) + '"'
