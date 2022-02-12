import cv2
import numpy
import pyautogui
import pytesseract
from time import sleep
from config import *
from link import *

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

pp = pyautogui.hotkey('win', 'd')

##открывает страницу мазилы
sleep(0.1)
mozila_x, mozila_y = pyautogui.locateCenterOnScreen('test1.png', grayscale=False)
pyautogui.doubleClick(mozila_x, mozila_y)


##ищет лупу для тыканья на поисковую строку
sleep(3)
loupe_x, loupe_y = pyautogui.locateCenterOnScreen('test2.png')



##
pyautogui.click(loupe_x + 50, loupe_y)
pyautogui.typewrite('https://translate.google.com/?hl=ru&sl=auto&tl=ru&op=translate')
pyautogui.hotkey('enter')




##перебор по массивы ссылок
for i in vanzai:

    ##открывает первую(вторую и тд. ссылку)
    new_tab_x, new_tab_y = pyautogui.locateCenterOnScreen('test4.png', grayscale=False)
    pyautogui.click(new_tab_x, new_tab_y)
    pyautogui.click(loupe_x + 50, loupe_y)
    pyautogui.typewrite(i)
    pyautogui.hotkey('enter')


    ##снимает название канала
    sleep(3)
    pyautogui.screenshot(r'foto2.png', region=(520, 450, 200, 50))
    img_for_name_chennel = cv2.imread('foto2.png')
    img_for_name_chennel = cv2.cvtColor(img_for_name_chennel, cv2.COLOR_BGR2RGB)
    name_chennel = pytesseract.image_to_string(img_for_name_chennel)


    ##снимает время публикации
    pyautogui.screenshot(r'foto.png', region=(420, 830, 200, 50))
    img = cv2.imread('foto.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(img, lang='rus')


    ##заменяет все ненужные символы и удаляет первый
    for t in tegs:
        text = text.replace(t, '')
    text = text.split()
    text.pop(0)


    ##заменяет чиcла на слова
    per = num.index(text[0], 0, len(name_num))

    if text[0] in num:
        text[0] = text[0].replace(text[0], name_num[per])
    print(text)

    ##КЛИКАЕТ НА ВИДЕО
    pyautogui.click(450, 750)
    sleep(1)
    pyautogui.click()
    sleep(0.5)

    ##берет имя видео
    pyautogui.screenshot(r'foto3.png', region=(95, 940, 1265, 30))
    img_name_video = cv2.imread('foto3.png')
    img_name_video = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    name_video = pytesseract.image_to_string(img_name_video, lang='eng')
    print(name_video)

    # 95 940
    # 1360 965

    #загоняет все в файл
    with open('rez_file.txt', 'a', encoding="utf-8") as f:
        f.write(name_chennel)
        for g in text:
            f.write(g + ' ')
        f.write(i + "\n")


cv2.waitKey(0)



