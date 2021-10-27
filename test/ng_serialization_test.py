# @author winily
# @date 2021-10-27
# Copyright©️ C++精修庙. All Rights Reserved

from serialization.ng_serialization import NgSerialization


def test():
    serialization = NgSerialization("./nginx.conf")
    print(serialization.read())


test()
