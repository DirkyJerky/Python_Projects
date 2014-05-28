from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time as ti

driver = webdriver.Firefox()
driver.get("http://family.bellingham.wa-k12.net/")
login = driver.find_element_by_xpath('//*[@id="login"]')
login.send_keys("roth ian000")
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys("2dez!te@")
driver.find_element_by_xpath('//*[@id="bLogin"]').click()

ti.sleep(3)

driver.switch_to_frame("Menu")



/html/body/table/tbody/tr/td/div[4]/a

https://www2.nwrdc.wa-k12.net/scripts/cgiip.exe/WService=wbellins71/sfwmnu04.w