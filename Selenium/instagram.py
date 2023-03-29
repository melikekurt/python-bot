from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
    
    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(2)
        
        usernameInput = self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(3)

        #self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]").click()

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)
        self.browser.find_element(By.CLASS_NAME,"_aacl _aacp _aacu _aacx _aad6 _aade").click()   #04.34
        
        time.sleep(3)

instagram = Instagram(username,password)
instagram.signIn()
instagram.getFollowers()