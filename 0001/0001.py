# -*- coding: UTF-8 -*-

"""
第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）
"""

import uuid

def createKey(number,length):
    Key = []
    for i in range(number):
        keyID = str(uuid.uuid4()).replace("-","").upper()[:length]
        if not keyID in Key:
            Key.append(keyID)

    return Key
if __name__ == "__main__":
    Key_list = createKey(200,8)
    for key in Key_list:
        print key
#    print createKey(200)