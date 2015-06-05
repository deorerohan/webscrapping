#! python3
# web scrapping.py - Downloads every single lefthandedtoons comic.

import requests, os, bs4, logging

logging.basicConfig(filename='lht/webscrapping.log', level=logging.INFO)
counter = 419
website = 'http://www.lefthandedtoons.com/'
# starting url
while counter > 0:
#if True:    
    # TODO: Download the page.
    print counter
    url = website + str(counter)
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    
    #print soup
    
    
    # TODO: Find the URL of the comic image.og:image 12345678    62984659  0
    comicElem = soup.select('#comicwrap img')
    
    #print '======================================='
    #print comicElem
  
    
    if comicElem == []:
         print('Could not find comic image.')
    else:
        try:
             comicUrl = comicElem[3].get('src')
             # Download the image.
             print('Downloading image %s...' % (comicUrl))
             res = requests.get(comicUrl)
             res.raise_for_status()
        except:
            comicUrl = ''
            
    # TODO: Download the image.
    
    # TODO: Save the image to ./xkcd.
    if comicUrl != '':
        imageFile = open(os.path.join('lht', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    print '======================================'
    # TODO: Get the Prev button's url.
    counter -=1
    
print('Done.')
