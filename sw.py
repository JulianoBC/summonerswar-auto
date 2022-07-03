#sw.py
from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con
import pydirectinput
import numpy
import mss
#startou = 0
time.sleep(1)
def moused():
    mouseDown()
    time.sleep(0.1)
    mouseUp()


def replayy():
    replay = pyautogui.locateCenterOnScreen('replay.png', region=(0, 0, 1920, 1080), grayscale=True, confidence=0.8)
    if replay is not None:
        pyautogui.moveTo(replay)
        sleep(0.5)
        pydirectinput.click()
        time.sleep(1)
        print('Cliquei direto no replay')

def main():
    repete = pyautogui.locateOnScreen('repeat1010.png', region=(0, 0, 1920, 1080), grayscale=True, confidence=0.8)
    if repete is not None:
            time.sleep(1)
            sell1 = pyautogui.locateCenterOnScreen('sell.png', region=(0, 0, 1920, 1080), grayscale=True, confidence=0.8)
            if sell1 is not None:
                pyautogui.moveTo(sell1)
                sleep(0.5)
                pydirectinput.click()
                time.sleep(1)
                #startou = startou + 1
                print(f'cliquei em vender')
                sell2 = pyautogui.locateCenterOnScreen('sell2.png', region=(0, 0, 1920, 1080), grayscale=True, confidence=0.8)
                if sell2 is not None:
                    pyautogui.moveTo(sell2)
                    sleep(0.5)
                    pydirectinput.click()
                    time.sleep(1)
                    print(f'cliquei em confirmar venda')
                    yesno = pyautogui.locateCenterOnScreen('yesno.png', region=(0, 0, 1920, 1080), grayscale=True, confidence=0.8)
                    if yesno is not None:
                        pyautogui.moveTo(yesno)
                        sleep(0.5)
                        pydirectinput.click()
                        time.sleep(1)
                        replayy()
                        print(f'cliquei em sim')
                        repeatb = pyautogui.locateCenterOnScreen('repeatb.png', region=(0, 0, 1920, 1080), grayscale=True, confidence=0.8)
                        if repeatb is not None:
                                pyautogui.moveTo(repeatb)
                                sleep(0.5)
                                pydirectinput.click()
                                sleep(0.5)
                                print('cliquem em repetir batalha')
                        else:
                                print('Não encontrei repetir batalha... esperando por 10 segundos')
                                sleep(10)
                        repeatb = pyautogui.locateCenterOnScreen('repeatb.png', region=(0, 0, 1920, 1080), grayscale=True, confidence=0.8)
                        if repeatb is not None:
                                pyautogui.moveTo(repeatb)
                                pydirectinput.click()
                                time.sleep(2)


def repetir():
    repeatb = pyautogui.locateCenterOnScreen('repeatb.png', region=(0, 0, 1920, 1080), grayscale=True, confidence=0.8)
    if repeatb is not None:
        pyautogui.moveTo(repeatb)
        pydirectinput.click()
        time.sleep(2)
        moused()
        time.sleep(20)



def repetir9():
    repetir9 = pyautogui.locateCenterOnScreen('repetir9.png', region=(0, 0, 1920, 1080), grayscale=True, confidence=0.8)
    if repetir9 is not None:
        pyautogui.moveTo(repetir9)
        sleep(1)
        pydirectinput.click()
        time.sleep(1)


def magic():
    magic = pyautogui.locateCenterOnScreen('magic.png', region=(0, 0, 1920, 1080), grayscale=True, confidence=0.8)
    if magic is not None:
            repb = pyautogui.locateCenterOnScreen('repb.png', region=(0, 0, 1920, 1080), grayscale=True, confidence=0.8)
            if repb is not None:
                pyautogui.moveTo(repb)
                sleep(1)
                pydirectinput.click()
                time.sleep(1)
            replayy()


while keyboard.is_pressed('q') == False:
    print('esperando para repetir batalha...10 segundos')
    time.sleep(1)
    replayy()
    magic()
    main()
    time.sleep(10)
    #repetir9()
    pass


#main()
#print('esperando para repetir batalha...')
