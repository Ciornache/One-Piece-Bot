from asyncio.windows_events import NULL
from hashlib import pbkdf2_hmac
from hmac import new
from http.client import NETWORK_AUTHENTICATION_REQUIRED
from multiprocessing.connection import wait
from re import search
from sqlite3 import paramstyle
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import json
import requests

driver = webdriver.Chrome(executable_path="chromedriver (1).exe")
users = []


class InstaBot:
    global users

    def LogIn(self):
        driver.get("https://www.instagram.com/")
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
        self.password.send_keys("")
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
        send = driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")
        good.send_keys(message)
        send.click()
        sleep(10)

    def SendMessages(self):
        for i in users:
            if i != "teodormarciuc" and i != "radu.ady.18":
                continue
            driver.get("https://www.instagram.com/direct/new/")
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")))
            notifButton = driver.find_element(
                By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
            notifButton.click()
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
                "THE ONE PIECE....... THE ONE PIECE IS REAAAAAL!!!!")
            self.SendRequestedMessage(
                "CAN WE GEEEEET MUCH HIGHEEEEEEER..... SO HIGHHHHHH. AW AW AW AAAA")
            self.SendRequestedMessage(
                "https://www.youtube.com/watch?v=qkZgtkIzXNM&ab_channel=JPMEMECLIPS")


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
