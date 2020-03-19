from random import randint, choice
from bs4 import BeautifulSoup
import requests
import pandas as pd
import urllib.request
import ctypes
from time import sleep
import os

#CONSTANTS
categories = ["aero-desktop-wallpapers","animals-desktop-wallpapers", "architecture-desktop-wallpapers", "army-desktop-wallpapers", "artistic-desktop-wallpapers",
"black_and_white-desktop-wallpapers", "cartoons-desktop-wallpapers", "celebrities-desktop-wallpapers", "charity-desktop-wallpapers",
"city-desktop-wallpapers", "computers-desktop-wallpapers", "cute-desktop-wallpapers", "elements-desktop-wallpapers", "food_and_drink-desktop-wallpapers",
"funny-desktop-wallpapers", "games-desktop-wallpapers", "girls-desktop-wallpapers", "holidays-desktop-wallpapers", "love-desktop-wallpapers",
"motors-desktop-wallpapers", "movies-desktop-wallpapers", "music-desktop-wallpapers", "nature-desktop-wallpapers", "seasons-desktop-wallpapers",
"space-desktop-wallpapers", "sports-desktop-wallpapers", "travel-desktop-wallpapers", "vintage-desktop-wallpapers"]
csvdata = pd.read_csv("data/data.csv")

def UpdateMaxPages():
    global categories
    data = open("data/data.csv", "w")
    data.write("category, maxpages\n")

    for x in categories:
        page = int(BeautifulSoup(requests.get("http://wallpaperswide.com/{}".format(x)).content, "html.parser").find_all("div", class_="pagination")[-1].find_all("a")[-2].text)
        data.write("{}, {}\n".format(x, page))
    data.close()

def MakeUrl():
    global categories, csvdata
    random_category = choice(categories)
    category_data, maxpage_data = list(csvdata["category"]), list(csvdata["maxpages"])
    random_page_num = randint(1, maxpage_data[category_data.index(random_category)])

    url = "http://wallpaperswide.com/{}/page/{}".format(random_category, random_page_num)

    return url

def ChooseRandomImage(url):
    page = requests.get(url).content
    object = BeautifulSoup(page, "html.parser")

    step1 = object.find_all("ul", class_="wallpapers")[1]
    step2 = step1.find_all("li", class_="wall")
    step3 = [x.find("a")["href"] for x in step2]

    return "http://wallpaperswide.com{}".format(choice(step3))

def DownloadImage(url):
    object = BeautifulSoup(requests.get(url).content, "html.parser").find("div", class_="wallpaper-resolutions").find_all("a")
    link = [x["href"] for x in object]
    urllib.request.urlretrieve("http://wallpaperswide.com{}".format(link[6]), "image/background.jpg")

def ChangeBackground(path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(path) , 0)
