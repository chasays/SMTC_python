import re, sys
from collections import  Counter


def staticsWords(fileName):
    pattern = r'[a-zA-Z0-9]+'
    with open(fileName) as f:
        wordsCount = re.findall(pattern, f.read())
    # return len(wordsCount)
    return Counter(wordsCount) #

if __name__=='__main__':
    filePath = sys.path[0] + '/word.txt'
    print staticsWords(filePath)
    sum = 0
    for key in staticsWords(filePath).keys():
        sum += staticsWords(filePath)[key]
    print sum