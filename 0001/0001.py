# -*- coding: UTF-8 -*-

"""
第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）
"""

import uuid

def createKey(number,length):
    Key = []
    for i in range(number):
        keyID = str(uuid.uuid4()).replace("-","").upper()[:length] #uuid4是uuid生成验证码中的一种方法，uuid4会有重复现象
        if not keyID in Key:
            Key.append(keyID)

    return Key
if __name__ == "__main__":
    Key_list = createKey(200,8)
    for key in Key_list:
        print key
        
#    print createKey(200)
# uuid1()——基于时间戳。由MAC地址、当前时间戳、随机数生成。可以保证全球范围内的唯一性，但MAC的使用同时带来安全性问题，局域网中可以使用IP来代替MAC
# uuid2()——基于分布式计算环境DCE（Python中没有这个函数）。算法与uuid1相同，不同的是把时间戳的前4位置换为POSIX的UID。实际中很少用到该方法
# uuid3()——基于名字的MD5散列值。通过计算名字和命名空间的MD5散列值得到，保证了同一命名空间中不同名字的唯一性，和不同命名空间的唯一性，但同一命名空间的同一名字生成相同的uuid
# uuid4()——基于随机数。由伪随机数得到，有一定的重复概率，该概率可以计算出来
# uuid5()——基于名字的SHA-1散列值。算法与uuid3相同，不同的是使用 Secure Hash Algorithm 1 算法
# 使用uuid生成的字符串使用"-"来 链接，所以需要用replace将"-"替换成""
