import requests, os, bs4

class magpi:
    """ class to download monsters comic"""
    
    def __init__ (self):
        """ Class initialiser """
        self.counter = 1
        self.url = 'https://www.raspberrypi.org/magpi-issues/MagPi' + '{0:02}'.format(self.counter) + '.pdf'
        self.absPath = os.path.dirname(os.path.abspath(__file__)) + '/magpi/'

    def DownloadPage(self):
        print('Downloading page %s...' % self.url)
        
    def IsPageDownloaded(self):
        return self.url + '\n' in self.listOflinks
        
    def DownloadComic(self):
        comicUrl = self.url
	print 'Downloading magazine %s ...' %(comicUrl)
	res = requests.get(comicUrl)
	res.raise_for_status()
        imageFile = open(os.path.join(self.absPath, os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        
        
    def WriteComicLink(self):
	print 'writing url'
        self.linksFile.write(self.url + '\n')
        
    def SetNextLink(self):
	print 'getting new url' 
        self.url = self.GetNextLink()
        
    def GetNextLink(self):
        self.counter += 1
        return 'https://www.raspberrypi.org/magpi-issues/MagPi' + '{0:02}'.format(self.counter) + '.pdf' 
        
    def GetDownloadedLinks(self):
	print 'readng file'
        myFile = open(self.absPath + 'links.txt', 'r')
        self.listOflinks = myFile.readlines()
        myFile.close()
#	print self. listOflinks
 #       self.url = self.listOflinks[len(self.listOflinks) - 1].strip()
#        self.counter = int(self.url[36:])
	print self.counter
        self.linksFile = open(self.absPath + 'links.txt', 'a')
        
    def IsThereNext(self):
        return True # There will always be some link
        
    def Done(self):
        self.linksFile.close()


print "Please run WebScrapping.py"
