# _*_ coding:utf-8 _*_
# @author winily
# @date 2021-10-29
# Copyright©️ C++精修庙. All Rights Reserved
# 解析模块的基础模块，所有的解析模块都要继承它
from serialization.utils import *


class NgParseModuleBase(object):
    # 它会传入一个字符串 key 提供匹配
    def set_match_and_parse(self, match_and_parse):
        self.__match_and_parse = match_and_parse

    def match_and_parse(self, key, config):
        self.__match_and_parse(key, config)

    def basic_parse(self, config_group):
        data = {}
        for item in config_group:
            item_key_value = parse_key_value(item)
            key = item_key_value['key']
            value = item_key_value['value']
            temp_value = self.__match_and_parse(key, value)
            if temp_value != False:
                value = temp_value

            if key in data:
                if isinstance(data[key], list):
                    data[key].append(value)
                else:
                    data[key] = [data[key], value]
            else:
                data[key] = value
        return data

    # 它会传入一个字符串 key 提供匹配
    def match_key(self, key):
        '''
        判断是否匹配你当前的解析器
        :Must return Boolen Type:
        '''

    # 顶层解析器会调用改方法获取到解析后的数据
    # def to_data(self, config):
    #     '''
    #     解析配置并返回配置对象
    #     :return config object.:
    #     '''
    def to_data(self, config):
        config = remove_external_brace(config)
        return self.basic_parse(divide_config(config))
