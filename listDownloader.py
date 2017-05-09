from getLinks import *
import sys
from bs4 import BeautifulSoup as bs
import dryscrape
from subprocess import call
def finalLink(arr):

    sample="http://en.savefrom.net/#url="+"http://youtube.com/watch?v=mzTc24c-Rd0&index=16&list=PLmXfFxjdp3CHCRpDULlvcaqWfK_zLPWF2"+"&utm_source=youtube.com&utm_medium=short_domains&utm_campaign=www.ssyoutube.com"
    file=open("Final"+filename,"wb")
    ll=len(arr)
    i=0
    while i < ll:
        session=dryscrape.Session()
        session.visit("http://en.savefrom.net/#url="+arr[i]+"&utm_source=youtube.com&utm_medium=short_domains&utm_campaign=www.ssyoutube.com")
        data=session.body()
        soup=bs(data,'html.parser')
        link=soup.find('a',title="video format: 720p")
        print link
        if link==None:
            continue
        print link['href']
        file.write(link['href']+"\n")
        i+=1
    file.close()

#youtube playlist link
# eg url="https://www.youtube.com/playlist?list=PLmXfFxjdp3CHCRpDULlvcaqWfK_zLPWF2"
url=str(sys.argv[1])
filename="list.txt"#str(sys.argv[2])
arr=getLinks(url,filename)
finalLink(arr)
