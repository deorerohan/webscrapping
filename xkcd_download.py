#!/usr/bin/env python
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

class xkcd:
    """ class to download XKCD comic"""
    def __init__ (self):
        """ Class initialiser """
        self.counter = 405
        #self.counter = 62
        self.url = 'http://xkcd.com/' + str(self.counter)            # starting url
        self.absPath = os.path.dirname(os.path.abspath(__file__)) + '/xkcd/'
        
    def DownloadPage(self):
        print('Downloading page %s...' % self.url)
        res = requests.get(self.url)
        res.raise_for_status()
        self.soup = bs4.BeautifulSoup(res.text)
        
    def IsPageDownloaded(self):
        return self.url + '\n' in self.listOflinks
        
    def DownloadComic(self):
        comicElem = self.soup.select('#comic img')
        
        if comicElem == []:
             print('Could not find comic image.')
        else:
             comicUrl = 'http:' + comicElem[0].get('src')
             
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
        self.url = self.GetNextLink()
        
    def GetNextLink(self):
        self.counter += 1
        return 'http://xkcd.com/' + str(self.counter) 
        
    def GetDownloadedLinks(self):
        myFile = open(self.absPath+'links.txt', 'r')
        self.listOflinks = myFile.readlines()
        myFile.close()
        self.url = self.listOflinks[-1].strip()
        self.counter = int(self.url[16:])
        print self.counter
        self.linksFile = open(self.absPath + 'links.txt', 'a')
        
    def IsThereNext(self):
        return True # There will always be some link
        
    def Done(self):
        self.linksFile.close()


print "Please run WebScrapping.py"

