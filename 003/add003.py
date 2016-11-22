import redis, os

HOST =  'localhost'
PORT = 6379

def generateCode(number):
    with open('code_200.txt', "wb") as f:
        for i in range(number):
            str = (''.join(map(lambda xx:(hex(ord(xx))[2:]),os.urandom(16))))
            f.write(str + '\n')
def saveDataToRedis(data):
    try:
        r = redis.Redis(HOST, PORT)
        for i in range(200):
            print  data[i].strip('\n')
            r.sadd("code", data[i].strip('\n'))
        r.save()
        print 'Done'
    except:
        print 'the end'

if __name__=="__main__":
    generateCode(200)
    with open('code_200.txt', 'r') as f:
        saveDataToRedis(f.readlines())