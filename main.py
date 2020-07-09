import pyautogui 
from PIL import Image, ImageGrab
#pip install pillow y pip install pyautogui

import time


def click(key):
    pyautogui.keyDown(key)
    return


def colision(data): 
    #colision para las aves
    for i in range (530,560):
        for j in range(80, 127):
            if data[i, j] < 171:
                click("down")
                return
    #colision para los cactus
    for i in range(530,560):
        for i in range(130,160):
            if data[i, j] < 100:
                click("up")
                return

    return

    


