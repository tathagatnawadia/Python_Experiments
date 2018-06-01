#THis is a comment

import os
import subprocess
import sys
import re
import shutil
global special
special = []

def to_dir(todir):
        print(todir)
        confirm = 'y'
        if os.path.exists(todir):
                confirm = input('Working directory contains a folder of same name !! OVERWRITE (y/n) ::: ')
        if confirm == 'n':
                print('Operation aborted')
                sys.exit(0)
        if not os.path.exists(str(todir)):
                os.mkdir(todir)
        for fpaths in special:
                name = os.path.basename(fpaths)
                shutil.copy(fpaths,os.path.join(todir,name))
                
def to_zip(tozip):
        print(tozip)
        confirm = 'y'
        if os.path.exists(str(tozip)+'.zip'):
                confirm = input('Working directory contains a zip of same name !! OVERWRITE (y/n)? ::: ')
        if confirm == 'n':
                print('Operation aborted')
                sys.exit(0)
        if not os.path.exists(str(tozip)+'.zip'):
                cmd = 'zip -j '+tozip+' '+ ' '.join(special)
                (status,output) = subprocess.getstatusoutput(cmd)
                if status:
                        print('OOPS !! Something went wrong while compressing the files')
                        sys.exit(1)
def checkspecial(dire):
        print(dire)
        filenames = os.listdir(dire)
        for filename in filenames:
                name = str(filename)
                match = re.search(r'__(\w+)__',name)
                if match:
                        special.append(os.path.abspath(os.path.join(dire,filename)))

def main():
        args = sys.argv[1:]
        if not args:
                print('Usage : [--tozip] [--todir] name dir dir dir')
                sys.exit(1)
        tozip = ''
        todir = ''
        print(args)
        if not args[1]:
                print('Usage : [--tozip] [--todir] name dir dir dir')
                sys.exit(1)
        if args[0] == '--todir':
                todir = args[1]
                del args[0:2]
        elif args[0] == '--tozip':
                tozip = args[1]
                del args[0:2]
        else:
                print('Usage : [--tozip] [--todir] name dir dir dir')
        for dir in args:
            checkspecial(dir)
        print(special)
            
        if todir:
                to_dir(todir)
        elif tozip:
                to_zip(tozip)
        print('You operation has been done succesfully !!')

if __name__ == '__main__':
        main()
                
