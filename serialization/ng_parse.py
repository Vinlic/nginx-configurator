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


class NgParse:
    def __init__(self, config):
        self.__config = config
        self.__parseModules = create_parse_modules()
        pass

    def __divide(self, config):

        result = []
        tempLine = []
        braceStack = []

        for item in config:
            tempLine.append(item)

            if item == LEFT_BRACE:
                braceStack.append(LEFT_BRACE)

            if item == RIGHT_BRACE:
                if braceStack[-1] == LEFT_BRACE:
                    braceStack.pop()
                else:
                    braceStack.append(RIGHT_BRACE)

                if len(braceStack) == 0:
                    result.append("".join(tempLine))
                    tempLine = []

            if len(braceStack) >= 2 and braceStack[-1] == RIGHT_BRACE and braceStack[-2] == LEFT_BRACE:
                braceStack.pop()
                braceStack.pop()
                if len(braceStack) == 0:
                    result.append("".join(tempLine))
                    tempLine = []
                # 导出最终数据对象

            if (item == SEMICOLON and len(braceStack) == 0):
                result.append("".join(tempLine))
                tempLine = []

        return result

    def to_data(self):
        divide_config = self.__divide(self.__config)
        for item in divide_config:
            print("-------------------")
            print(item)
