# Author: James Grace from various others
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class AoCHelper:
    def __init__(self, wdPath):
        self.__driver = webdriver.Chrome(executable_path=wdPath)

    def __get_driver(self):
        return self.__driver

    def loginTwitter(self, usrName, passWd):
        driver = self.__get_driver() # get driver variable
        driver.get("https://adventofcode.com/2021/auth/twitter") # direct to page
        usrNameForm = driver.find_element(By.NAME, "session[username_or_email]")
        passWdForm = driver.find_element(By.NAME, "session[password]")
        usrNameForm.send_keys(usrName)
        passWdForm.send_keys(passWd)
        driver.find_element(By.ID, "allow").click()

    def loginGitHub(self, usrName, passWd):
        driver = self.__get_driver() # get driver variable
        driver.get("https://adventofcode.com/2021/auth/github") # direct to page
        usrNameForm = driver.find_element(By.ID, "login_field")
        passWdForm = driver.find_element(By.ID, "password")
        usrNameForm.send_keys(usrName)
        passWdForm.send_keys(passWd)
        driver.find_element(By.NAME, "commit").click()


    def getInputToArray(self, day):
        driver =  self.__get_driver()
        inputUrl = "https://adventofcode.com/2021/day/"+str(day)+"/input"
        driver.get(inputUrl)
        filteredSrc = driver.page_source.replace('<html><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">', "")
        filteredSrc = filteredSrc.replace('</pre></body></html>', "")
        return filteredSrc.split("\n")[0:-1] # split on newline (0 -> -1 to avoid inevitable blank last element)

    def uploadAnswer(self, day, answer):
        driver = self.__get_driver()
        driver.get("https://adventofcode.com/2021/day/" + str(day))
        try:
            answerForm = driver.find_element(By.NAME, "answer")
            answerForm.send_keys(str(answer))
            driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
        except NoSuchElementException:
            print("no answer box, meaning both challenges already complete")
            return True
        try:
            driver.find_element(By.CLASS_NAME, "day-success")
            return True
        except NoSuchElementException:
            return False

