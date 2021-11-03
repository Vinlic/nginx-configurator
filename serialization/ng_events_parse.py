# _*_ coding:utf-8 _*_
# @author winily
# @date 2021-10-29
# Copyright©️ C++精修庙. All Rights Reserved
# 解析 events 配置

from serialization.ng_parse_module_base import NgParseModuleBase
from serialization.utils import *


class NgEventsParse(NgParseModuleBase):
    def match_key(self, key):
        return key == 'events'

    # def to_data(self, config):
    #     config = remove_external_brace(config)
    #     return self.basic_parse(divide_config(config))
