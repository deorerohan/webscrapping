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


def getNextLink(soup):
	return soup.select('#comic a')[0].get('href')



url = 'http://www.peppertop.com/greys/comic/yeti-boots/'              # starting url
#url = 'http://www.peppertop.com/greys/comic/spider-grey/'

linksFile = open('greys/links.txt', 'r')
listOflinks = linksFile.readlines()
linksFile.close()

linksFile = open('greys/links.txt', 'a')

#os.makedirs('xkcd', exist_ok=True)   # store comics in ./xkcd
#while not url.endswith('#'):
while True:
    # TODO: Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    
    # Get the Prev button's url.
    nextLink = getNextLink(soup)
    print nextLink
    
    if url in listOflinks:
		url = nextLink
		print 'continuing'
		#exit()
		continue
		
    
    print '==============================='

    comicElem = soup.select('#comic img')
    print comicElem
    
    if comicElem == []:
         print('Could not find comic image.')
    else:
         comicUrl = comicElem[0].get('src')
         comicUrl = 'http:' + comicUrl
         # Download the image.
         print('Downloading image %s...' % (comicUrl))
         res = requests.get(comicUrl)
         res.raise_for_status()
         
    imageFile = open(os.path.join('greys', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    linksFile.write(url)
    url = nextLink

linksFile.close()

print('Done.')

