# _*_ coding:utf-8 _*_
# @author winily
# @date 2021-10-27
# Copyright©️ C++精修庙. All Rights Reserved

# 把 nginx 配置文件序列化成对象
from ng_parse_modules import create_parse_modules


class NgParse:
    def __init__(self, config):
        self.config = config
        self.parseModules = create_parse_modules()
        pass

    # 导出最终数据对象
    def to_data(slef):
        pass
