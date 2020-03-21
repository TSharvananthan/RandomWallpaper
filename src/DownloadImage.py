import os
from bs4 import BeautifulSoup
from requests import get
from urllib.request import urlretrieve

def DownloadImage(url):
    object = BeautifulSoup(get(url).content, "html.parser").find("div", class_="wallpaper-resolutions").find_all("a")
    link = [x["href"] for x in object]
    try:
        urlretrieve("http://wallpaperswide.com{}".format(link[6]), "image/background.jpg")
    except:
        os.mkdir("image")
        urlretrieve("http://wallpaperswide.com{}".format(link[6]), "image/background.jpg")
        
