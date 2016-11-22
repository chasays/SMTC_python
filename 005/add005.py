import re, sys

def staticsWords(fileName):
    pattern = r'[a-zA-Z0-9]+'
    with open(fileName) as f:
        wordsCount = re.findall(pattern, f.read())
    return len(wordsCount)

if __name__=='__main__':
    filePath = sys.path[0] + '/word.txt'
    print staticsWords(filePath)