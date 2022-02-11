from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from termcolor import colored
import sys
from termcolor import colored, cprint
from colors import *
print(color(
    '''
  ██████  ██░ ██  ▄▄▄       ██▀███  ▓█████  ▄▄▄▄    ▒█████  ▄▄▄█████▓
▒██    ▒ ▓██░ ██▒▒████▄    ▓██ ▒ ██▒▓█   ▀ ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ▓██ ░▄█ ▒▒███   ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
  ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄ ▒██░█▀  ▒██   ██░░ ▓██▓ ░ 
▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒░██▓ ▒██▒░▒████▒░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░▒░▒   ░   ░ ▒ ▒░     ░    
░  ░  ░   ░  ░░ ░  ░   ▒     ░░   ░    ░    ░    ░ ░ ░ ░ ▒    ░      
      ░   ░  ░  ░      ░  ░   ░        ░  ░ ░          ░ ░           
                                                 ░                   
'''
, fg='red'
))

print('creds to: https://github.com/xtekky')

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://zefoy.com/")

vidUrl = input("url: ")

def loop1():
    global i
    sleep(10)
    try:
        driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[5]/div/button").click()
    except:
        print("Solve Captcha!, Refreshing...")
        driver.refresh()
        loop1()
    try:
        sleep(0.5)
        driver.find_element(By.XPATH, "/html/body/div[4]/div[6]/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[4]/div[6]/div/form/div/div/button").click()
        sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[4]/div[6]/div/div/div[1]/div/form/button").click()
        sleep(3)
        driver.refresh()
        i += 1
        total = i * 500
        print("Success delivered!")
        sleep(1)
        loop1()
    except:
        print("Timer still running, trying again in a minute")
        driver.refresh()
        sleep(5)
        loop1()


bot = int(input("Type 1 to start\n"))


if bot == 1:
    print('starting engine...')
    loop1()
else:
    print('error')
