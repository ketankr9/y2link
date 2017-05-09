from getLinks import *
import sys
from bs4 import BeautifulSoup as bs
import dryscrape
from subprocess import call
from  urllib2 import urlopen
#youtube playlist link
# url=str(sys.argv[1])
# filename=str(sys.argv[2])
# url="https://www.youtube.com/playlist?list=PLmXfFxjdp3CHCRpDULlvcaqWfK_zLPWF2"

def finalLink(arr):
    sample="http://en.savefrom.net/#url="+"http://youtube.com/watch?v=mzTc24c-Rd0&index=16&list=PLmXfFxjdp3CHCRpDULlvcaqWfK_zLPWF2"+"&utm_source=youtube.com&utm_medium=short_domains&utm_campaign=www.ssyoutube.com"
    ll=1
    i=0
    downloadLink=""
    while i < ll:
        session=dryscrape.Session()
        session.visit("http://en.savefrom.net/#url="+arr+"&utm_source=youtube.com&utm_medium=short_domains&utm_campaign=www.ssyoutube.com")
        data=session.body()
        soup=bs(data,'html.parser')
        link=soup.find('a',title="video format: 720p")
        # print link
        if link==None:
            continue
        print link['href']
        downloadLink=link['href']
        i+=1
    call(["aria2c","-x","16","-s","16",downloadLink])


#youtube video link
url=str(sys.argv[1])
finalLink(url)
