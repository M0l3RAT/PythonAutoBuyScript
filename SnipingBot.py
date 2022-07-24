from selenium import webdriver
from time import sleep

class ProcessorBot():
    def __init__(self):
        self.driver = webdriver.Firefox()

    def login(self):
        self.driver.get('https://www.amazon.com')
        #the sleep is long enough for you to sign in
        sleep(50)

    def checkAndBuy(self):
        self.driver.get('https://www.amazon.com/AMD-Ryzen-5600X-12-Thread-Processor/dp/B08166SLDF/ref=as_li_ss_tl?_encoding=UTF8&psc=1&refRID=46SVCMBX83Z462G6B1R7&ascsub&linkCode=sl1&tag=fixitservices-20&linkId=4a7a15114b861372c3e24f9bb3547fd7&language=en_US')
        sleep(1)   
        try:
            buyNow = self.driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')
            #remove the comments on the clicks for it to actually buy.
            #buyNow.click() 
            sleep(2)
            buyNow2 = self.driver.find_element_by_xpath('//*[@id="hlb-ptc-btn"]')
            #buyNow2.click()
            sleep(2)
            buyNow3 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/form/div/div/div/div[2]/div/div[1]/div/div[1]/div/span/span/input')  
            #buyNow3.click()
            sleep(1)
            self.driver.close()
        except Exception as e:
            print(e)
            sleep(1.5)
            self.checkAndBuy()
bot = ProcessorBot()
bot.login()
bot.checkAndBuy()

#change the checkandbuy url to change the item your buying, must be an amazon link





