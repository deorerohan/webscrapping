#!/usr/bin/env python

import greys
import fullcircle
import monsters
import lefthandedtoons
import xkcd_download
import magpi


case = 1
while case < 7:
    if case ==1:    
        # To Download Greys
        scrap = greys.greys()
    elif case ==2 :
        # To Download Monsters
        scrap = monsters.monsters()
    elif case ==3:
        # To Download Left handed toons
        scrap = lefthandedtoons.lefthandedtoons()
    elif case ==4:
        # To Download XKCD comic
        scrap = xkcd_download.xkcd()
    elif case == 5:
        # To Download Full Circle
        scrap = fullcircle.fullcircle()
    elif case == 6:
	# To download MagPi
	scrap = magpi.magpi()
    #elif case == 7:
        # bolkya resha
    else :
		break
    
    #if debuggin use this
    if case != 6:
		case +=1 
		continue
        
    try:
        scrap.GetDownloadedLinks()
        while(scrap.IsThereNext()):
            scrap.DownloadPage()
            if scrap.IsPageDownloaded():
                print "Page already downloaded"
                scrap.SetNextLink()
                continue
            print 'Downloading something...'
            scrap.DownloadComic()
            scrap.WriteComicLink()
            scrap.SetNextLink()
    except:
        print "Closing"
        scrap.Done()

    print 'Downloading completed!!'
    case += 1
