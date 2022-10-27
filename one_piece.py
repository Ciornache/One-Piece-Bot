from asyncio.windows_events import NULL
from hashlib import pbkdf2_hmac
from hmac import new
from http.client import NETWORK_AUTHENTICATION_REQUIRED
from multiprocessing.connection import wait
from re import search
from sqlite3 import paramstyle
from tkinter import CURRENT
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import json
import requests
from PIL import Image
from selenium.webdriver import ActionChains
import pyautogui
driver = webdriver.Chrome(executable_path="chromedriver (1).exe")
users = []

actions = ActionChains(driver)


class InstaBot:

    global users

    def __init__(self):
        driver.get("https://www.instagram.com/")
        driver.maximize_window()

    def LogIn(self):

        sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div")))
        self.cookieButton = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]")
        self.cookieButton.click()
        self.username = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
        self.password = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
        self.go = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div")
        self.username.send_keys("monkeydluffy565656")
        self.password.send_keys("gigolo69")
        sleep(5)
        try:
            self.go.click()
        except (ElementClickInterceptedException):
            sleep(1)
            self.LogIn()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/section/div/button")))

    def GetUsers(self, profilePage):
        driver.get("https://www.instagram.com/{}/".format(profilePage))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
            By.CLASS_NAME, "_ac2a")))
        followers = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a/div")
        followers.click()
        sleep(2)
        while 1:
            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{}]/div[2]/div[1]/div/div/span/a/span/div".format(len(users) + 1))))
            except (TimeoutException):
                break
            username = driver.find_element(
                By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{}]/div[2]/div[1]/div/div/span/a/span/div".format(len(users) + 1))
            users.append(username.text)
            driver.execute_script(
                "arguments[0].scrollIntoView();", username)

    def create(self, name, input):
        file = open(name, "w")
        json.dump(input, file, indent=0)

    def load(self, name):
        f = open("usernames.json")
        data = json.load(f)
        f.close()
        return data

    def SendRequestedMessage(self, message):
        good = driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
        good.send_keys(message)
        send = driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")
        send.click()
        sleep(10)

    def SendMessages(self):
        for i in users:
            driver.get("https://www.instagram.com/direct/new/")
            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")))
                notifButton = driver.find_element(
                    By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
                notifButton.click()
            except (TimeoutException):
                pass
            sleep(10)
            searchUser = driver.find_element(
                By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input")
            searchUser.send_keys(i)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/button")))
            available = driver.find_element(
                By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/button")
            available.click()
            sleep(10)
            goTo = driver.find_element(By.CLASS_NAME, "_aagz")
            goTo.click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")))
            self.SendRequestedMessage(
                "THE ONE PIECEEEE....... THE ONE PIECE IS REAAAAAL!!!!")
            self.SendRequestedMessage(
                "CAN WE GEEEEET MUCH HIGHEEEEEEER..... SO HIGHHHHHH..... AW AW AW AAAAHHHH")
            self.SendRequestedMessage(
                "https://www.youtube.com/watch?v=qkZgtkIzXNM&ab_channel=JPMEMECLIPS")
            self.SendImage(
                "https://static.wikia.nocookie.net/onepiece/images/b/b7/Edward_Newgate_Anime_Infobox.png/revision/latest?cb=20220926165737")
            sleep(3)

    def SendImage(self, link):
        self.driver.get(
            "{}".format(link))
        self.actions.context_click(driver.find_element(
            By.XPATH, "/html/body/img")).perform()
        pyautogui.moveTo(700, 670, duration=1)
        pyautogui.click()
        pyautogui.moveTo(60, 75)
        pyautogui.click()
        sleep(2)
        pyautogui.moveTo(900, 920)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'v')
        self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/button").click()
        sleep(10)


# Initialize Bot
Luffy = InstaBot()

# Log into Account
Luffy.LogIn()

# Collect the Users
Luffy.GetUsers("candalesilviu123")

# Store the Users in a JSON(Javascript Object Notation)
Luffy.create("usernames.json", users)

# Retrieves the Users from the JSON
users = Luffy.load("usernames.json")

# Send the messages
Luffy.SendMessages()

# Process Finished
driver.close()

# TO DO : Filter the users that have already received a message -> Only send to new users
#         If a user responds back, add him back to the desired user list( send a new message : eg -> Do you wanna join my crew? :) )
