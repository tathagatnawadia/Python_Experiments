#This is comment

import sys
import codecs
import re
global db
db={}


def cat(filename1,filename2):
    f=open(filename1,'r')
    g=open(filename2, 'w')
    i=0
    j=0
    for s in f:
        match = re.search('\w+',s)
        db[i]=match.group()
        print(match.group())
        i=i+1
    print(db)
    print('The number of words processed is ',len(db))
    for j in range(len(db)):
        g.write(db[j]+'\n')
    f.close()
    g.close()
def main():
    cat(sys.argv[1],sys.argv[2])


if __name__ == '__main__':
    main()

