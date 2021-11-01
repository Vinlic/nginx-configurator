# _*_ coding:utf-8 _*_
# @author winily
# @date 2021-10-27
# Copyright©️ C++精修庙. All Rights Reserved

# 把 nginx 配置文件序列化成对象
from serialization.ng_parse_modules import create_parse_modules
from serialization.public_symbol import *
from serialization.utils import *


class NgParse:
    def __init__(self, config):
        self.__config = config
        self.__match_and_parse = create_parse_modules()
        pass

    def to_data(self):
        config_group = divide_config(self.__config)
        # self.__match_and_parse("http", divide_config[2])
        data = {}
        for item in config_group:
            item_key_value = parse_key_value(item)
            key = item_key_value['key']
            value = item_key_value['value']
            if is_brace(value):
                value = self.__match_and_parse(key, value)

            data[key] = value

        print(data)

        return data
