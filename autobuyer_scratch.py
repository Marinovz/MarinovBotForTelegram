from selenium import webdriver

import time


class Autobuyer():
    def __init__(self,url,email,password,random_name):
        self.url = url
        self.info = buyerScratcher(self,email,password,random_name)
        #self.status = getStatus()
        
        #buyerScratcher()
        
def buyerScratcher(self,email,password,random_name):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(self.url + "/admin/login")
    driver.find_element_by_name('email').send_keys(email)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_name('remember').click()
    driver.find_element_by_xpath("//button[contains(.,'Login')]").click()
    dailyProfit = driver.find_element_by_xpath(("//table[@class='table table-bordered table-striped']/tbody/tr/td[5]")).text
    allTimeProfit = driver.find_element_by_xpath(("//table[@class='table table-bordered table-striped']/tbody/tr/td[6]")).text
    balance = driver.find_element_by_xpath(("//table[@class='table table-bordered table-striped']/tbody/tr/td[7]")).text
    driver.get(self.url + "/admin/transactions")
    driver.implicitly_wait(10)
    time.sleep(3)
    driver.save_screenshot(random_name + '.png')
    driver.get(self.url + "/admin/accounts")
    driver.implicitly_wait(10)
    status = driver.find_element_by_xpath(("//div[@class='col-sm-12']/table/tbody/tr/td[7]")).text
    driver.close()  
    return dailyProfit, allTimeProfit,balance, status

