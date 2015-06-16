#!/usr/bin/env python


#import greys
#import fullcircle
#import monsters
#import lefthandedtoons
import xkcd_download

# To Download Greys
#scrap = greys.greys()


# To Download Full Circle
#scrap = fullcircle.fullcircle()

# To Download Monsters
#scrap = monsters.monsters()

# To Download Left handed toons
#scrap = lefthandedtoons.lefthandedtoons()

# To Download XKCD comic
scrap = xkcd_download.xkcd()

scrap.GetDownloadedLinks()

try:
    while(scrap.IsThereNext()):
        scrap.DownloadPage()
        if scrap.IsPageDownloaded():
            print "Page already downloaded"
            scrap.SetNextLink()
            continue
            
        scrap.DownloadComic()
        scrap.WriteComicLink()
        scrap.SetNextLink()
except:
    print "Closing"
    scrap.Done()

print 'Downloading completed!!'
    
