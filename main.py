import RandomWallpaper
from time import sleep

def Main():
    works = False
    while works == False:
        try:
            BACKGROUND_IMAGE_PATH = "image/background.jpg"
            link = RandomWallpaper.MakeUrl()
            image = RandomWallpaper.ChooseRandomImage(link)
            RandomWallpaper.DownloadImage(image)
            RandomWallpaper.ChangeBackground(BACKGROUND_IMAGE_PATH)
            works = True
        except:
            print("ERROR, WAITING 5 SECONDS BEFORE TRYING AGAIN")
            sleep(5)
            continue

Main()
