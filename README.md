# PyBillboard 
Billboard webscraper to filter top 100 list by artist name
    
Webpage being scrapped: https://www.billboard.com/charts/hot-100
        
    HTML Item structure

    (button) chart-element__wrapper -  whole one box
        (span) chart-element__rank - song rank
        (span) chart-element__information - info box
            (span) chart-element__information__song - song name
            (span) chart-element__information__artist - artist


Project details:

    Data object -

    songs_list = {'rank': ('song name','artist')}
    
