import sys

def write():
    print('Creating new text file') 

    name = input('Enter name of text file: ')+'.txt'

    try:
        file = open(name,'w')   # Trying to create a new file or open one
        file.close()

    except:
        print('Something went wrong! Can\'t tell what?')
        sys.exit(0) # quit Python
def main:
    write()

if __name__ == '__main__':
    main()
    
