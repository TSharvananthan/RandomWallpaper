from src.UpdateMaxPages import UpdateMaxPages
from src.MakeUrl import MakeUrl
from src.ChooseRandomImage import ChooseRandomImage
from src.DownloadImage import DownloadImage
from src.ChangeBackground import ChangeBackground
from time import sleep

def RandomWallpaper():
  works = False
  while works == False:
    try: 
      BACKGROUND_IMAGE_PATH = "image/background.jpg"
      UpdateMaxPages()
      url = MakeUrl()
      image = ChooseRandomImage(url)
      DownloadImage(image)
      ChangeBackground(BACKGROUND_IMAGE_PATH)
      works = True
    except:
      print("ERROR, WAITING 5 SECONDS BEFORE TRYING AGAIN")
      sleep(5)
      continue
