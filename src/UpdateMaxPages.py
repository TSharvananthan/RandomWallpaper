from bs4 import BeautifulSoup
from requests import get

def UpdateMaxPages():
    categories = ["aero-desktop-wallpapers","animals-desktop-wallpapers", "architecture-desktop-wallpapers", 
    "army-desktop-wallpapers", "artistic-desktop-wallpapers",    "black_and_white-desktop-wallpapers", 
    "cartoons-desktop-wallpapers", "celebrities-desktop-wallpapers", "charity-desktop-wallpapers", 
    "city-desktop-wallpapers", "computers-desktop-wallpapers", "cute-desktop-wallpapers", "elements-desktop-wallpapers", 
    "food_and_drink-desktop-wallpapers",    "funny-desktop-wallpapers", "games-desktop-wallpapers", 
    "girls-desktop-wallpapers", "holidays-desktop-wallpapers", "love-desktop-wallpapers", 
    "motors-desktop-wallpapers", "movies-desktop-wallpapers", "music-desktop-wallpapers", "nature-desktop-wallpapers", 
    "seasons-desktop-wallpapers",    "space-desktop-wallpapers", "sports-desktop-wallpapers", 
    "travel-desktop-wallpapers", "vintage-desktop-wallpapers"]
    data = open("data/data.csv", "w")
    data.write("category,maxpages\n")

    for x in categories:
        page = int(BeautifulSoup(get("http://wallpaperswide.com/{}".format(x)).content, "html.parser").find_all("div", class_="pagination")[-1].find_all("a")[-2].text)
        data.write("{}, {}\n".format(x, page))
    data.close()
