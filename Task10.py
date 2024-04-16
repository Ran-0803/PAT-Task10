from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from time import sleep

class Extract():

    def __init__(self):
        self.url = "https://www.instagram.com/guviofficial/"
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

    def clickElementByXpath(self,Xpath):
        # This method is used to find the element by its ID
        return self.driver.find_element(by=By.XPATH,value=Xpath).click()

    def findElementByXpath(self,XPATH):
        # This method is used to find element by its Xpath
        return self.driver.find_element(by=By.XPATH, value=XPATH).text

    def boot(self):
        self.driver.get(self.url)
        sleep(5)
        self.driver.maximize_window()
        sleep(3)

    def quit(self):
        self.driver.quit()


    def getFollowersAndFollowing(self):
        # This is used to close the popup message
        self.clickElementByXpath('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/nav/div[2]/div/div/div[2]/div/div/div[1]/div/button/span')
        sleep(3)
        # This is used to find and print the number of followers
        print(" The Numbers of Followers in Guvi: ",self.findElementByXpath("/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button/span/span"))
        # This is used to find and print the numbers of following
        print(" The Number of Following in Guvi: ", self.findElementByXpath("/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button/span/span"))

obj = Extract()
obj.boot()
obj.getFollowersAndFollowing()
obj.quit()




