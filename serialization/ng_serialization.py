# @author winily
# @date 2021-10-27
# Copyright©️ C++精修庙. All Rights Reserved

# 序列化 nginx 配置将文件序列化成 对象 或者 将对象序列化成配置文件

class NgSerialization:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        config_file = open(self.file_path)
        config = config_file.readlines()
        config_file.close()
        return config

    def write(self, config):
        pass
