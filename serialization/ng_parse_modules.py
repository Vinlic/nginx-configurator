# _*_ coding:utf-8 _*_
# @author winily
# @date 2021-10-29
# Copyright©️ C++精修庙. All Rights Reserved
from serialization.ng_parse_module_base import NgParseModuleBase


# 利用反射获取 NgParseModuleBase 的所有子类，并且实例化
# NgParseModuleBase 的子类要被装载到当前目录的 __init__.py 中

def create_parse_modules():
    module_lits = NgParseModuleBase.__subclasses__()
    serialization_model = __import__("serialization")

    parse_modules = []

    def match_and_parse(key, config):
        for module in parse_modules:
            if module.match_key(key):
                return module.to_data(config)
        return False

    for module in module_lits:
        subclass = getattr(serialization_model, module.__name__)
        sub_obj = subclass()
        parse_modules.append(sub_obj)
        sub_obj.set_match_and_parse(match_and_parse)

    return match_and_parse
