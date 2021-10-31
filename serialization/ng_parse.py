# _*_ coding:utf-8 _*_
# @author winily
# @date 2021-10-27
# Copyright©️ C++精修庙. All Rights Reserved

# 把 nginx 配置文件序列化成对象
from serialization.ng_parse_modules import create_parse_modules


# cosnt var
SEMICOLON = ";"
LEFT_BRACE = "{"
RIGHT_BRACE = "}"


def equals(a, b):
    return a == b


class NgParse:
    def __init__(self, config):
        self.__config = config
        self.__parseModules = create_parse_modules()
        pass

    def __divide(self, config):

        result = []
        tempLine = []
        braceStack = []
        braceStatucs = False

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
                result.append("".join(tempLine))
                tempLine = []
                braceStatucs = False

            # 匹配 ; 模式分块
            if item == SEMICOLON and braceStatucs == False:
                result.append("".join(tempLine))
                tempLine = []

        return result

    def to_data(self):
        divide_config = self.__divide(self.__config)
        for item in divide_config:
            print("-------------------")
            print(item)
