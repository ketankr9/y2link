from bs4 import BeautifulSoup as bs
from  urllib2 import urlopen
import sys
#youtube playlist link
# url=str(sys.argv[1])
# filename=str(sys.argv[2])
# url="https://www.youtube.com/playlist?list=PLmXfFxjdp3CHCRpDULlvcaqWfK_zLPWF2"
def getLinks(url,filename):
    data=urlopen(url).read()
    soup=bs(data,'html.parser')
    tb=soup.find('tbody',id="pl-load-more-destination")
    count=-1
    li=[]
    for i in tb.children:
        count+=1
        if count%2==1:
            li.append(i)
    links=[]
    file=open(filename,"wb")
    for tr in li:
        st=str(tr.find('td',class_='pl-video-title').find('a')['href'])
        file.write("https://www.youtube.com"+st+"\n")
        links.append("www.youtube.com"+st)
    file.close()
    return links
