#import beautiful soup
from bs4 import BeautifulSoup as soup
# import urlopen
from urllib.request import urlopen as urlo
# import pprint
import pprint as pp

# URL to billboard current billboard top 100
page_url = "https://www.billboard.com/charts/hot-100"

# open connection and download html
page_request = urlo(page_url)

# parse html into a soup data structure to be able to traverse html
page_soup = soup(page_request.read(), "html.parser")

# close connection
page_request.close()

## TEST: print out soup contents to verify data
pp(page_soup)