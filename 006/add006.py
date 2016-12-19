import re, sys, os
from collections import Counter
#
FILE_PATH = sys.path[0]
def staticsWords(fileName):
    pattern = r'''[a-zA-Z]+|\$?\d+%?$'''
    with open(fileName) as f:
        wordsCount = re.findall(pattern, f.read())
    return Counter(wordsCount)

stopWords = ['the', 'in', 'of', 'and', 'to', 'has', 'that', 's', 'is', 'are', 'a', 'with', 'as', 'an']

def run(FILE_PATH):
    os.chdir(FILE_PATH)
    totalWords = Counter()
    for i in os.listdir(os.getcwd()):
        if os.path.splitext(i)[1] == '.txt':
            totalWords += staticsWords(i)

    for i in stopWords:
        totalWords[i] = 0
    return totalWords.most_common()[0][0]

if __name__=='__main__':
    print run(FILE_PATH)