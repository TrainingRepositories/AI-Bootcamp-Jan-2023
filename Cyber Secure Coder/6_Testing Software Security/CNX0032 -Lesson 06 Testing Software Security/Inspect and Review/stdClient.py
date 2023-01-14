'''
HTTP Client Requester
'''

import urllib
import time

def GetURL(url):
    ''' input url to request, returns response'''
    try:
        filehandle = urllib.urlopen(url)
        contents = filehandle.read()
        print("Contents: ", contents)
        return contents
    except Exception as err:
        return err

def main():
    ''' no input or output'''
    
    # Mark the starting time of the main loop
    print("Starting Client ....")
    
    for i in range(0,10):
        response = GetURL('http://127.0.0.1:8000/')
        print(response)

if __name__ == '__main__':
    main()
