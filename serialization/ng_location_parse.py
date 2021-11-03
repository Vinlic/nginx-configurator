# _*_ coding:utf-8 _*_
# @author winily
# @date 2021-10-29
# Copyright©️ C++精修庙. All Rights Reserved
# 解析 location 配置

from serialization.ng_parse_module_base import NgParseModuleBase
from serialization.utils import *


class NgLocationParse(NgParseModuleBase):
    def match_key(self, key):
        return key == 'location'

    def to_data(self, config):
        location_routing_config = parse_key_value(config)
        location_config = remove_external_brace(location_routing_config['value'])
        return {
            'routing': location_routing_config['key'],
            'config': self.basic_parse(divide_config(location_config))
        }
