#!/usr/bin/env python

# web scrapping.py - Downloads every single lefthandedtoons comic.

import requests, os, bs4


class lefthandedtoons:
    """ class to download Left Handed Toons comic"""
    
    def __init__ (self):
        """ Class initialiser """
        #self.counter = 1
        self.counter = 62
        self.url = 'http://www.lefthandedtoons.com/' + str(self.counter)            # starting url
        
    def DownloadPage(self):
        print('Downloading page %s...' % self.url)
        res = requests.get(self.url)
        res.raise_for_status()
        self.soup = bs4.BeautifulSoup(res.text)
        
    def IsPageDownloaded(self):
        return self.url + '\n' in self.listOflinks
        
    def DownloadComic(self):
        comicElem = self.soup.select('#comicwrap img')
        
        if comicElem == []:
             print('Could not find comic image.')
        else:
             comicUrl = comicElem[3].get('src')
             print('Downloading image %s...' % (comicUrl))
             res = requests.get(comicUrl)
             res.raise_for_status()
             
        imageFile = open(os.path.join('lht', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        
        
    def WriteComicLink(self):
        self.linksFile.write(self.url + '\n')
        
    def SetNextLink(self):
        self.url = self.GetNextLink()
        
    def GetNextLink(self):
        self.counter += 1
        return 'http://www.lefthandedtoons.com/' + str(self.counter) 
        
    def GetDownloadedLinks(self):
        myFile = open('lht/links.txt', 'r')
        self.listOflinks = myFile.readlines()
        myFile.close()
        self.linksFile = open('lht/links.txt', 'a')
        
    def IsThereNext(self):
        return True # There will always be some link
        
    def Done(self):
        self.linksFile.close()


print "Please run WebScrapping.py"