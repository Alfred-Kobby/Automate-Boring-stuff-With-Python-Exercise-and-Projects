from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')
linkElem = browser.find_element(By.LINK_TEXT, 'Read Online for Free')
linkElem.click()
browser.quit()