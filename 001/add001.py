#!/usr/bin/env python
#coding: utf-8

# import random, string, sys
#
# field = string.letters + string.digits
# filePath = sys.path[0]
# with open((filePath + '/code.txt'), 'wb') as f:
#     f.write("ssss\n")
#     f.readline()

import random, os
def generateCode(number):
    with open('code_200.txt', "wb") as f:
        for i in range(number):
            str = (''.join(map(lambda xx:(hex(ord(xx))[2:]),os.urandom(16))))
            f.write(str + '\n')


if __name__=="__main__":
    print generateCode(200)

# def getRandom():
#     return "".join(random.sample(field, 4))
#
# def concatenate(group):
#     return "-".join(getRandom() for i in range(group))
#
#
# def generate(n):
#     return [concatenate(4) for i in range(n)]
#
# if __name__=='__main__':
#     print generate(200)
