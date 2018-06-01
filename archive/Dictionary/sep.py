import sys

def count(filename):
    f=open(filename,'r')
    count=0
    for s in f:
        count=count+1
    print(count)
def main():
    count(sys.argv[1])
if __name__ == '__main__':
    main()
