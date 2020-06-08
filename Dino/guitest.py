# website: https://chromedino.com/#
# zoom: 125
import pyautogui
from PIL import Image,ImageGrab
#from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    #for cactus
    for i in range(200,330):
        for j in range(470,535):
            if data[i,j] < 100:
                hit("up")
                return
                
    #for birds
    for i in range(150,200):
        for j in range(350,465):
            if data[i,j] < 100:
                hit("down")
                return

    #for Game Over
    for i in range(400,900):
        for j in range(350,400):
            if data[i,j]<100:
                exit()

    return

if __name__ == "__main__":
    print("Hey.. Dino will run in 2 sec")
    time.sleep(2)
    #hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
        '''
        #for cactus
        for i in range(200,330):
            for j in range(470,535):
                data[i,j]=0

        #for birds
        for i in range(150,200):
            for j in range(350,465):
                data[i,j]=171

        #for Game Over
        for i in range(400,900):
            for j in range(350,400):
                data[i,j]=200
        image.show()
        break
        '''