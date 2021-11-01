# _*_ coding:utf-8 _*_
# @author winily
# @date 2021-10-29
# Copyright©️ C++精修庙. All Rights Reserved
# 解析 http 配置

from serialization.ng_parse_module_base import NgParseModuleBase
from serialization.utils import *


class NgHttpParse(NgParseModuleBase):
    def match_key(self, key):
        return key == 'http'

    def to_data(self, config):
        config = remove_external_brace(config)
        data = {}
        for item in divide_config(config):
            item_key_value = parse_key_value(item)
            key = item_key_value['key']
            value = item_key_value['value']
            if is_brace(value):
                value = self.to_data(value)
            data[key] = value
        return data
