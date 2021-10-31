# _*_ coding:utf-8 _*_
# @author winily
# @date 2021-10-27
# Copyright©️ C++精修庙. All Rights Reserved

# 序列化 nginx 配置将文件序列化成 对象 或者 将对象序列化成配置文件

from serialization.ng_parse import NgParse

class NgSerialization:
    def __init__(self, file_path):
        self.__file_path = file_path

    def read(self):
        config_file = open(self.__file_path)
        config = config_file.readlines()
        config_file.close()
        config = self.__remove_note_and_blank_line(config)

        NgParse("".join(config)).to_data()

        return ''.join(config)
        # return NgParse(config).to_data()

    def __remove_note_and_blank_line(self, config):
        result = []
        for item in config:
            temp = item.strip()
            if len(temp) <= 0 or temp[0] == "#":
                continue
            result.append(item)
        return result

    def write(self, config):
        pass
