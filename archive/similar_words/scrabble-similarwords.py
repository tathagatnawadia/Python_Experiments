#This makes out words and find similar words of the entered word in the dictionary

import sys
import re
global guess
guess={}

def getmatches(filename,combi):
    f=open(filename, 'r')
    combi=combi.upper()
    i=0
    j=0
    conf=0
    print('Length of string you enter',len(combi),combi)
    for s in f:
        j=0
        for j in range(len(combi)):
            if combi[j] in s:
                conf=1
            else:
                conf=0
                break
        if conf == 1:
            print('There was a match')
            print(s)
            guess[i]=s
            i=i+1
            
def main():
    getmatches(sys.argv[1],sys.argv[2])
    print(guess)

if __name__ == '__main__':
    main()
