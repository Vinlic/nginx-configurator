# _*_ coding:utf-8 _*_
# @author winily
# @date 2021-11-01
# Copyright©️ C++精修庙. All Rights Reserved

# 一些工具方法

from serialization.public_symbol import *

# 分切配置块 获取到 {} 整段配置或者 ；分割的每行配置
def divide_config(config):

    result = []
    tempLine = []
    braceStack = []
    braceStatucs = False

    def get_value(value_arr):
        if value_arr[0] == '\n':
            value_arr = value_arr[1:]
        return "".join(value_arr).strip()

    for item in config:
        tempLine.append(item)

        # 如果是左括号就压入栈
        if item == LEFT_BRACE:
            braceStack.append(LEFT_BRACE)
            braceStatucs = True

        # 如果是右括号
        # 如果栈内上一个刚好是左括号 就从栈中弹出一个，匹配正确 {}
        # 如果不是，就将右括号也压入栈内
        if item == RIGHT_BRACE:
            if braceStack[-1] == LEFT_BRACE:
                braceStack.pop()
            else:
                braceStack.append(RIGHT_BRACE)

        # 匹配 {} 模式分块
        if len(braceStack) == 0 and braceStatucs:
            result.append(get_value(tempLine))
            tempLine = []
            braceStatucs = False

        # 匹配 ; 模式分块
        if item == SEMICOLON and braceStatucs == False:
            result.append(get_value(tempLine))
            tempLine = []

    return result


# 分切配置 key 和 value
def parse_key_value(config):
    if config[-1] == SEMICOLON:
        config = config[0:-1]

    key = config[0: config.index(' ')]
    value = config[config.index(' '):]
    value = value.strip()
    return {'key': key, 'value': value}


# 是否是 {} 配置块
def is_brace(value):
    return value[0] == LEFT_BRACE and value[-1] == RIGHT_BRACE


# 消除最外层 {}
def remove_external_brace(value):
    if is_brace(value):
        value = value[1: -1].strip()

    return value
