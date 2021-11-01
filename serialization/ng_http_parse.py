# _*_ coding:utf-8 _*_
# @author winily
# @date 2021-10-29
# Copyright©️ C++精修庙. All Rights Reserved
# 解析 http 配置

from serialization.ng_parse_module_base import NgParseModuleBase


class NgHttpParse(NgParseModuleBase):
    def match_key(self, key):
        return key == 'http'

    def to_data(self, config):
        print("parse data http")
        self.match_and_parse("events", config)
        return config
