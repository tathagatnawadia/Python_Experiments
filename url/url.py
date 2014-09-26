#This is a program which retrieves the html code of a url from a server
#This way we can play with the html of 

import sys
import os 
import subprocess
import shutil
import urllib
import urllib.request  #We just used this because urllib is not independent
import urllib.response

def htmlcode(url):
        url = 'http://'+url
        html = urllib.request.urlopen(url)
        """Tathagat Nawadia help :: htmlcode('google.com/edu') -----> returns the entire html code as text
        use text.read() to see the code !!! Have funn 
        This function indirectly uses the "urllib.request.urlopen" to get your job don
        You dont have to necessarily begin the url with "https://" because this function already does that"""
        return html
if __name__ == '__main__':
        main()
        
  
