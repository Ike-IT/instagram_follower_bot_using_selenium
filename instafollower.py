from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from random import *


SIMILAR_ACCOUNT = Your Choice IG Handle
USERNAME = Your Username
PASSWORD = Your Password


SERVICE_OBJ = Service("\C:\Development\chromedriver_win32")
INSTAGRAM_URL = "https://www.instagram.com/"


""" D blocks of codes below prevents D browser 4rm closing automatically """
options = Options()
options.AddExcludedArgument("enable-automation")
options.add_experimental_option("detach", True)


class Instafollower:

    def __init__(self):
        self.driver = webdriver.Chrome(service=SERVICE_OBJ, options=options)

    def login(self):
        self.driver.get(INSTAGRAM_URL)
        time.sleep(10)
        accept_cookies = self.driver.find_element(By.CLASS_NAME, "_a9--")
        accept_cookies.click()
        time.sleep(4)
        self.driver.find_element(By.NAME, 'username').send_keys(USERNAME)
        self.driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
        time.sleep(6)
        save_info_button = self.driver.find_element(By.CLASS_NAME, '_acan')
        save_info_button.click()
        time.sleep(6)
        notification_button = self.driver.find_element(By.CLASS_NAME, '_a9--')
        notification_button.click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")
        time.sleep(5)
        scroll_bar = self.driver.find_element(By.CLASS_NAME, "_aano")
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_bar)

    def follow(self):
        # Random time between a follow click cycle, to seem more human
        delay = randint(2, 8)
        time.sleep(delay)
        time.sleep(2)
        followers_list = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[45]/div[3]/button')
        if followers_list.text == "Follow":
            followers_list.click()
        else:
            pass





