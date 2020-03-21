from requests import get
from bs4 import BeautifulSoup

def ChooseRandomImage(url):
    page = get(url).content
    object = BeautifulSoup(page, "html.parser")

    step1 = object.find_all("ul", class_="wallpapers")[1]
    step2 = step1.find_all("li", class_="wall")
    step3 = [x.find("a")["href"] for x in step2]

    return "http://wallpaperswide.com{}".format(choice(step3))
