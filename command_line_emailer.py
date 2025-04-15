#! python3
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

username = input("Enter your email username\n")
password = input("Enter your email password\n")
recipient_email = input("Enter recipient email\n")
subject = input("Enter subject of mail\n")
message = input("Enter message\n")

browser = webdriver.Firefox()
browser.get('https://gmail.com')

wait = WebDriverWait(browser, 30)

email_input = wait.until(EC.presence_of_element_located((By.ID, "identifierId")))
email_input.send_keys(username)

next_button = browser.find_element(By.ID, 'identifierNext')
next_button.click()

password_input = wait.until(EC.visibility_of_element_located((By.NAME, "Passwd")))
password_input.send_keys(password)

# next_button = wait.until(EC.element_to_be_clickable((By.ID, "passwordNext")))
next_button = browser.find_element(By.ID, 'passwordNext')
next_button.click()

# continue_button = browser.find_element(By.XPATH, "//button[.//span[text()='Continue']]")
# continue_button.click()
# time.sleep(10)
#
compose_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Compose']")))
compose_button.click()
time.sleep(10)

to_input = wait.until(EC.visibility_of_element_located((By.ID, ":bc")))
to_input.send_keys(recipient_email)

subject_input = wait.until(EC.visibility_of_element_located((By.NAME, "subjectbox")))
subject_input.send_keys(subject)

message_input = wait.until(EC.visibility_of_element_located((By.ID, ":90")))
message_input.send_keys(message)

submit_button = wait.until(EC.visibility_of_element_located((By.ID, ":7a")))
submit_button.click()
print("Email sent")
browser.quit()