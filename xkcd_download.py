#!/usr/bin/env python
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

class xkcd:
     """ class to download XKCD comic"""
    
    def __init__ (self):
        """ Class initialiser """
        self.counter = 1
        #self.counter = 62
        self.url = 'http://xkcd.com/' + str(self.counter)            # starting url
        
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
             comicUrl = comicElem[0].get('src')
             print('Downloading image %s...' % (comicUrl))
             res = requests.get(comicUrl)
             res.raise_for_status()
             
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
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
        myFile = open('xkcd/links.txt', 'r')
        self.listOflinks = myFile.readlines()
        myFile.close()
        self.linksFile = open('xkcd/links.txt', 'a')
        
    def IsThereNext(self):
        return True # There will always be some link
        
    def Done(self):
        self.linksFile.close()


print "Please run WebScrapping.py"


url = 'http://xkcd.com'              # starting url
#os.makedirs('xkcd', exist_ok=True)   # store comics in ./xkcd
#while not url.endswith('#'):
if True:
    # TODO: Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    
    print soup
    
    print '==============================='
    
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
    
    print url
    
    print '==============================='
    
    
    
    
    # TODO: Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    print comicElem
    
    if comicElem == []:
         print('Could not find comic image.')
    else:
         comicUrl = comicElem[0].get('src')
         # Download the image.
         print('Downloading image %s...' % (comicUrl))
         res = requests.get(comicUrl)
         res.raise_for_status()


    # TODO: Download the image.

    # TODO: Save the image to ./xkcd.
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
    
    print url
    # TODO: Get the Prev button's url.

print('Done.')
