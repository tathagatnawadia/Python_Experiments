#This is comment

import os
import re

def main():
    a = ['aaaa','bb','ccccccc','ddd']
    b = [len(s) for s in a]
    print('Value of original list',a)
    print('Comprehended list',b)

    c = [s for s in os.listdir('.') if re.search(r'.exe',s)]
    print('This script runs in the current working directory to pull out the .exe files and store their names in the list')
    print(c)

if __name__ == '__main__':
    main()
