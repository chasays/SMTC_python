#!/usr/bin/env python
#coding: utf-8
import random, os, MySQLdb
def generateCode(number):
    with open('code_200.txt', "wb") as f:
        for i in range(number):
            str = (''.join(map(lambda xx:(hex(ord(xx))[2:]),os.urandom(16))))
            f.write(str + '\n')
def saveDataToSQL(data):
    try:
        conn = MySQLdb.connect(host='localhost', user='root', passwd='ssssssdf', db='test', port=3306)
        cur = conn.cursor()
        for i in range(200):
            command = 'INSERT INTO code (code) VALUES (\'%s\')' % data[i].strip('\n')
            cur.execute(command)
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

if __name__=="__main__":
    generateCode(200)
    with open('code_200.txt', 'r') as f:
        saveDataToSQL(f.readlines())
