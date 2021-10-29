# _*_ coding:utf-8 _*_
# @author winily
# @date 2021-10-29
# Copyright©️ C++精修庙. All Rights Reserved
# 解析模块的基础模块，所有的解析模块都要继承它

class NgParseModuleBase:
    # 它会传入一个字符串 key 提供匹配
    def match_key(self, key):
        '''
        判断是否匹配你当前的解析器
        :Must return Boolen Type:
        '''

    # 顶层解析器会调用改方法获取到解析后的数据
    def to_data(self):
        '''
        解析配置并返回配置对象
        :return config object.:
        '''