

# link http://fullcirclemagazine.org/issue-48/
# name : _en.epub


import requests, os, bs4

class fullcircle:
    """ class to download Full Circle Magzine"""
    
    def __init__ (self):
        """ Class initialiser """
        self.counter = 1
        self.url = 'http://fullcirclemagazine.org/issue-' + str(self.counter)             # starting url
        self.nextLink = 'temp'
        
    def DownloadPage(self):
        print('Downloading page %s...' % self.url)
        res = requests.get(self.url)
        res.raise_for_status()
        self.soup = bs4.BeautifulSoup(res.text)
        
    def IsPageDownloaded(self):
        return self.url + '\n' in self.listOflinks
        
    def DownloadComic(self):
        comicElem = self.soup.find_all('a')
        
        if comicElem == []:
             print('Could not find magzine epub.')
        else:
            indx = 0
            while 'en.epub' not in comicElem[indx].get('href'):
                indx += 1
            
            comicUrl = comicElem[indx].get('href')
            print('Downloading epub %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
             
        imageFile = open(os.path.join('fullcircle', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        
        
    def WriteComicLink(self):
        self.linksFile.write(self.url + '\n')
        
    def SetNextLink(self):
        self.url = self.GetNextLink()
        
    def GetNextLink(self):
        self.counter += 1
        return 'http://fullcirclemagazine.org/issue-' + str(self.counter)
        
    def GetDownloadedLinks(self):
        myFile = open('fullcircle/links.txt', 'r')
        self.listOflinks = myFile.readlines()
        myFile.close()
        self.linksFile = open('fullcircle/links.txt', 'a')
        
    def IsThereNext(self):
        return True # There will always be some link
        
    def Done(self):
        self.linksFile.close()


print "Please run WebScrapping.py"
