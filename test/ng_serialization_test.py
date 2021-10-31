# _*_ coding:utf-8 _*_
# @author winily
# @date 2021-10-27
# Copyright©️ C++精修庙. All Rights Reserved
import sys
sys.path.append("/Users/winily/Projects/Open-Source/nginx-configurator/")
from serialization.ng_serialization import NgSerialization


def test():
    serialization = NgSerialization(
        "/Users/winily/Projects/Open-Source/nginx-configurator/test/nginx.conf")
    config = serialization.read()
    # print(config)


test()
