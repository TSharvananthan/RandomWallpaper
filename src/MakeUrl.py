from random import choice, randint
import pandas as pd 

def MakeUrl():
    categories = ["aero-desktop-wallpapers","animals-desktop-wallpapers", "architecture-desktop-wallpapers", 
    "army-desktop-wallpapers", "artistic-desktop-wallpapers",    "black_and_white-desktop-wallpapers", 
    "cartoons-desktop-wallpapers", "celebrities-desktop-wallpapers", "charity-desktop-wallpapers", 
    "city-desktop-wallpapers", "computers-desktop-wallpapers", "cute-desktop-wallpapers", "elements-desktop-wallpapers", 
    "food_and_drink-desktop-wallpapers",    "funny-desktop-wallpapers", "games-desktop-wallpapers", 
    "girls-desktop-wallpapers", "holidays-desktop-wallpapers", "love-desktop-wallpapers", 
    "motors-desktop-wallpapers", "movies-desktop-wallpapers", "music-desktop-wallpapers", "nature-desktop-wallpapers", 
    "seasons-desktop-wallpapers",    "space-desktop-wallpapers", "sports-desktop-wallpapers", "travel-desktop-wallpapers", 
    "vintage-desktop-wallpapers"]
    csvdata = pd.read_csv("src/data/data.csv")
    
    random_category = choice(categories)
    category_data, maxpage_data = list(csvdata["category"]), list(csvdata["maxpages"])
    random_page_num = randint(1, maxpage_data[category_data.index(random_category)])

    url = "http://wallpaperswide.com/{}/page/{}".format(random_category, random_page_num)

    return url
