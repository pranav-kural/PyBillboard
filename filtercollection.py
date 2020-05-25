

# import reduce function
from functools import reduce

#import RegEx
import re


# search for a name inside a collection of names
def containsName(items_collection: list, filter_values: str):
    """ 
    Returns true if provided string value exists in the provided list collection.
    
    String value provided can have multiple alphanumeric characters or words, separated by spaces.
    
    Function will do a whole match for the string value provided. If any element of the string value
    provided is not found in the items collection list, function returns False and stops.
    
    Args:
        items_collection: List of elements in which the value will be searched
        filter_values: A single string with one or more words separated by spaces
        
    Returns:
        True: if match found
        False: if match not found 
    """
    
    # split string values by spaces and store in a list
    filter_values_list: list = filter_values.split(" ")
    
    # Split all elements of items_collection into separate elements without spaces in between
    # store in one single list
    items: list = reduce(lambda a,b: a + " " + b, items_collection).split(" ")
    
    # result store, False by default
    result: bool = False
    
    # check for each value in values provided to match
    for filter_value in filter_values_list:
            if filter_value in items:
                result = True
            else:
                return False
                break           # end loop no need to proceed
            
    # return the result
    return result        
        
            
""" 
Example -

from filterCollection import containsName as fd

>>> fd(['abc'],'abc')
True
>>> fd(['abc fgh'],'abc')
True
>>> fd(['abc fgh'],'abc fgh')
True
>>> fd(['abc fgh'],'abc son fgh')
False
>>> fd(['abc fgh sona'],'abc fgh')
True
>>> fd(['abc fgh sona'],'abc fgh sona')
True
>>> fd(['abc fgh sona'],'abc fgh sona trump')
False
"""


# cleanse data, remove unwanted character from artists names in songs collection
# return a list of artist names
def getArtistsNames(song_artist_info: str):
    return [artist_name.strip() for artist_name in re.split('&|Featuring| x ', song_artist_info)]


# Get a filtered list of songs out of all songs based on artist's name
def getArtistsSongsList(songs_collection: dict, artist_name: str):
    
    return dict(
        filter(
            lambda song_item: 
                containsName(getArtistsNames(song_item[1][1]), artist_name),
            songs_collection.items()
        )
    )