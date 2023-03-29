from githubUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Github:
    def __init__(self,username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []
    
    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        username = self.browser.find_element(By.XPATH,"//*[@id='login_field']")
        password = self.browser.find_element(By.XPATH,"//*[@id='password']")

        username.send_keys(self.username)
        password.send_keys(self.password)

        time.sleep(2) 

        self.browser.find_element(By.XPATH,"//*[@id='login']/div[4]/form/div/input[11]").click()

    def getFollowers(self):
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        time.sleep(2)

        items = self.browser.find_elements(By.XPATH,"//*[@id='user-profile-frame']/div/div[1]")

        for i in items:
            self.followers.append(i.find_element(By.XPATH,"//*[@id='user-profile-frame']/div/div[1]/div[2]/a/span[2]").text)

github = Github(username,password)
github.signIn()
github.getFollowers()
print(github.followers)