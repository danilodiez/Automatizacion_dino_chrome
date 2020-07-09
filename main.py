import pyautogui 
from PIL import Image, ImageGrab
#pip install pillow y pip install pyautogui

import time


def click(key):
    pyautogui.keyDown(key)
    return


def colision(data): 
    #colision para las aves
    for i in range (660, 720):
        for j in range(480, 530):
            if data[i, j] < 100:
                click("down")
                return
    
    #colision para los cactus
    for i in range(660, 720):
        for j in range(370, 410):
            if data[i, j] < 120:
                click("up")
                return 

    return

if __name__ == "__main__":
    time.sleep(5)
    click("up")

while True:
    imagen = ImageGrab.grab().convert('L')
    data = imagen.load()
    # Aca sacamos captura para ver la combinacion ideal de pixeles
    '''for i in range(660, 720):
        for j in range(370, 410):
            data[i, j] = 0
    imagen.show()
    break'''
    colision(data)
    
    

