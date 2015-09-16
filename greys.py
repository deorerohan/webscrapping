#!/usr/bin/env python

# link : http://www.peppertop.com/greys/comic/yeti-boots/
# This is first comic and there after we need to download
# there should be some check to avoid loading pages for which downloads
# are completed
# All scrapping projects should be kept in single file 
# but divided into different classes 
# so that common codes and functionalities such as check for previous downloads
# can go in different classed

import requests, os, bs4

class greys:
    """ class to download greys comic """
    
    def __init__ (self):
        """ Class initialiser """
        #self.url = 'http://www.peppertop.com/greys/comic/yeti-boots/'              # starting url
        self.url = 'http://www.peppertop.com/greys/comic/teenagers/'
        self.nextLink = 'temp'
        self.absPath = os.path.dirname(os.path.abspath(__file__)) + '/greys/'
        
    def DownloadPage(self):
        print('Downloading page %s...' % self.url)
        res = requests.get(self.url)
        res.raise_for_status()
        self.soup = bs4.BeautifulSoup(res.text)
        
    def IsPageDownloaded(self):
        return self.url + '\n' in self.listOflinks
        
    def DownloadComic(self):
        comicElem = self.soup.select('#comic img')
        #print comicElem
        
        if comicElem == []:
             print('Could not find comic image.')
        else:
             comicUrl = comicElem[0].get('src')
             comicUrl = 'http:' + comicUrl
             print('Downloading image %s...' % (comicUrl))
             res = requests.get(comicUrl)
             res.raise_for_status()
             
        imageFile = open(os.path.join(self.absPath, os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        
        
    def WriteComicLink(self):
        self.linksFile.write(self.url + '\n')
        
    def SetNextLink(self):
        self.url = self.nextLink = self.GetNextLink()
        
    def GetNextLink(self):
        comicElem = self.soup.select('#comic a')
        if comicElem == []:
            return ''
        else:
            return comicElem[0].get('href')
        
    def GetDownloadedLinks(self):
        myFile = open(self.absPath + 'links.txt', 'r')
        self.listOflinks = myFile.readlines()
        myFile.close()
        self.url = self.listOflinks[len(self.listOflinks) - 1].strip()
        self.linksFile = open(self.absPath + 'links.txt', 'a')
        
    def IsThereNext(self):
        return self.nextLink is not ''
        
    def Done(self):
        self.linksFile.close()


print "Please run WebScrapping.py"
