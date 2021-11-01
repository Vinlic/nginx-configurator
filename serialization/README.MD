### 当前为序列化模块目录

- 1.如何写一个新的解析模块

> 所有的解析模块都需要继承 NgParseModuleBase 父类
> 这个父类包含了 两个待实现方法和两个内置方法
> 
> 待实现方法：
>> match_key: params(key: string)
>> 用于匹配当前配置 key 是否合适当前模块，如果合适则将调用该模块
>> 的 to_data 进行解析配置，需要返回 Boolen 结果
> 
>> to_data: params(config: string)
>> 用于获取被解析后的结果数据，将会传入 config 字符串，需要返回被
>> 序列化成对象的值
> 
> 内置方法
> 
>> set_match_and_parse: params(match_and_parse: function)
>> 提供设置匹配解析方法，
>> 该方法会在 ng_parse_modules 模块中被创建。
>> 该方法主要的作用是匹配所有的解析模块，寻找到合适的解析模块就会
>> 调用该模块的 to_data 进行解析，然后返回被解析后的数据对象
>> 如果没有匹配的解析模块，将直接返回 config 字符串
> 
>> match_and_parse
>> 该方法就是调用了以上设置的 匹配解析函数 返回被解析后的数据对象
> 
> 继承了 NgParseModuleBase 父类的解析模块还需要添加到
> 当前目录的 \_\_init\_\_.py 中,如果不添加到该文件中，
> ng_parse_modules 内将无法获取到该解析模块。
> 
> 最终继承了 NgParseModuleBase 父类以及添加到 \_\_init\_\_.py
> 的解析模块会被 ng_parse_modules 中以反射的手段获取到，并且提供
> 给 match_and_parse 方法可进行调用匹配配置和解析配置

