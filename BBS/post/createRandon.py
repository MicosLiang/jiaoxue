#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

class RandomString:
    chars = {
        'upper': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'lower': 'abcdefghijklmnopqrstuvwxyz',
        'digit': '0123456789',
    }

    def __init__(self, length, *contents):
        self.kinds = {}
        self.length = length
        if len(contents) == 0:
            self.kinds = None
        else:
            for content in contents[0]:
                kind = content.split(':')[0]
                if len(content.split(':')) == 1:
                    self.kinds[kind] = 0
                else:
                    self.kinds[kind] = int(content.split(':')[1])

    def create(self):
        res = ''
        charset = ''
        if self.kinds is None:
            charset = ''.join(c for c in RandomString.chars.values())
        else:
            if self.length < sum(num for num in rs.kinds.values()):
                print('规则不符，生成失败。')
            else:
                for kind, num in rs.kinds.items():
                    if num == 0:
                        pass
                    else:
                        for i in range(num):
                            res += random.choice(RandomString.chars[kind])
                    charset += RandomString.chars[kind]
        for i in range(self.length - len(res)):
            res += random.choice(charset)
        str_list = list(res)
        random.shuffle(str_list)
        return ''.join(str_list)
