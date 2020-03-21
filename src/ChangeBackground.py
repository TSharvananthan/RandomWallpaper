import os
import ctypes

def ChangeBackground(path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(path) , 0)
        
