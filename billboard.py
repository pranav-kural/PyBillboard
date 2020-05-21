#import beautiful soup
from bs4 import BeautifulSoup as soup
# import urlopen
from urllib.request import urlopen, Request
# import pprint
import pprint as pp

# URL to billboard current billboard top 100
page_url = "https://www.billboard.com/charts/hot-100"

# add header to fake as if the request being made by a known browser
# to bypass mod_security - https://stackoverflow.com/a/16627277/5834653
page_request = Request(page_url, headers={'User-Agent': 'Mozilla/5.0'})

# open connection and download html
client_object = urlopen(page_request)

# parse html into a soup data structure to be able to traverse html
page_soup = soup(client_object.read(), "html.parser")

# close connection
client_object.close()

## TEST: print out title from soup contents to verify data loaded successfully
print(page_soup.title)