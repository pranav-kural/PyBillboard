#import beautiful soup
from bs4 import BeautifulSoup as soup
# import urlopen
from urllib.request import urlopen, Request
# import pprint
from pprint import pprint as pp

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
print(page_soup.title.text.replace('100', '10'))


""" 
Item structure

(button) chart-element__wrapper -  whole one box
	(span) chart-element__rank - song rank
	(span) chart-element__information - info box
		(span) chart-element__information__song - song name
		(span) chart-element__information__artist - artist

Data object -

filtered_songs_list = {'rank': ('song','artist')}
"""

# get all song items
all_songs = page_soup.findAll("button", "chart-element__wrapper")

# define list to hold all songs
songs_list = list()

# get details for each song
for song in all_songs:
    
    # song rank
    song_rank = song.find("span", "chart-element__rank__number").text
    
    # song name
    song_name = song.find("span", "chart-element__information__song").text
    
    # song artist name
    song_artist = song.find("span", "chart-element__information__artist").text
    
    # add it to the list
    songs_list.append({
        song_rank:
        (
            song_name, song_artist
        )
    })
    
# print out top 10 songs
pp(songs_list[:10])

# Next steps:
# 1. Filter out songs based on artist name provided over command line as argument
# 2. Print out the resulting list in a good format
# 3. Write the result to a file
# 
# 4. In future, if possible - 
#    Create a web implmenentation of this
#
# Misc
#
# song output formating note
# song item = f'{song_rank: <4} |  {song_name: <30} | {song_artist: <30}'