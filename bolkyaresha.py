import requests, os, bs4, logging

'''copied 156 images till with previous button http://www.bolkyaresha.marathi-unlimited.in/rakhi-pornima-bolkya-resha/
now i will have to try next button from current location
'''

logging.basicConfig(filename='resha/webscrapping.log', level=logging.INFO)

website = 'http://www.bolkyaresha.marathi-unlimited.in/page/'
counter = 1
url = 'http://www.bolkyaresha.marathi-unlimited.in/mala-room-hawi-ahe/'
absPath = os.path.dirname(os.path.abspath(__file__)) + '/resha/'
while True:
#while counter <= 10:
#if True:
    print counter
    logging.info('%d : %s' % (counter, url))
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    
    # TODO: Find the URL of the comic image.og:image 12345678    62984659  0
    div = soup.findAll("div", { "class" : "entry clearfix" })
    
    comicUrl = div[0].find('a')['href']
    #print comicUrl

    # Download the image.
    print('Downloading image %s...' % (comicUrl))
    res = requests.get(comicUrl)
    res.raise_for_status()

    imageFile = open(os.path.join(absPath, os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    print '======================================'
    # TODO: Get the Prev button's url.
    counter +=1
    prevLink = soup.select('a[rel="next"]')[0]
    url = prevLink['href']
    #print url
    #url = 'http://xkcd.com' + prevLink.get('href')
    

print('Done.')
