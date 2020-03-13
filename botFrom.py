import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import Data


class FormBot():
    def login(self):
        self.driver.get(Data.URL)

    def __init__(self):
        options = Options()
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(chrome_options=options, executable_path='chromedriver.exe')

    def randomtemperature(self):
        generatedvalue = random.randint(3, 8)
        return generatedvalue

    def randomStar(self):
        return random.randint(1, 2)

    def fillin(self):
        fieldnamelastname = self.driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div/div/div/input')
        fieldnamelastname.send_keys(Data.nameandlastname)
        fieldnumberroom = self.driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[3]/div/div/div/input')
        fieldnumberroom.send_keys(Data.numberroom)
        fieldoftemperature = self.driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[3]/div[2]/div[3]/div/div/div/input')
        fieldoftemperature.send_keys(Data.partofrandomtemperature+str(self.randomtemperature()))
        if(self.randomStar()==2):
            fieldrate = self.driver.find_element_by_xpath(
                '/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div/div/div/div[1]/span[5]')
            fieldrate.click()
        else:
            fieldrate1 = self.driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div/div/div/div[1]/span[4]')
            fieldrate1.click()

        fielddescriptin = self.driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[5]/div[2]/div[3]/div/div/div/textarea')
        fielddescriptin.send_keys(Data.discription)
        buttontsend = self.driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div/button/div')
        time.sleep(random.randint(60, 300))
        buttontsend.click()
        time.sleep(15)


#bot = FormBot()
#bot.login()
#bot.fillin()


