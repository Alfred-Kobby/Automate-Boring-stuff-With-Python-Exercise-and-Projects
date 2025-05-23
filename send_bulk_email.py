import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def extract_emails(file_path):
    df = pd.read_excel(file_path)
    return df.iloc[:, 0].dropna().tolist()  # grab first column, remove NaNs


# Load emails
emails = extract_emails("emails.xlsx")
bcc_string = ", ".join(emails)

# Launch browser
driver = webdriver.Firefox()
driver.get("https://mail.google.com")

# Wait for Gmail to load
wait = WebDriverWait(driver, 30)

email_input = wait.until(EC.presence_of_element_located((By.ID, "identifierId")))
email_input.send_keys("email")

next_button = driver.find_element(By.ID, 'identifierNext')
next_button.click()

password_input = wait.until(EC.visibility_of_element_located((By.NAME, "Passwd")))
password_input.send_keys("password")

# next_button = wait.until(EC.element_to_be_clickable((By.ID, "passwordNext")))
next_button = driver.find_element(By.ID, 'passwordNext')
next_button.click()

# Wait for the Compose button and click
compose_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.T-I.T-I-KE.L3")))
compose_btn.click()

# Wait for the compose window to appear
wait.until(EC.visibility_of_element_located((By.NAME, "to")))

# Click the "BCC" link to reveal the field
driver.find_element(By.XPATH, "//span[text()='Bcc']").click()

# Step 1: Expand the Bcc field if not already visible
try:
    bcc_toggle = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-tooltip='Add Bcc recipients ‪(⌘⇧B)‬']")))
    bcc_toggle.click()
    time.sleep(1)
except:
    print("BCC field might already be visible.")

# Step 2: Locate the input field with aria-label="BCC recipients"
try:
    bcc_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='BCC recipients']")))
    bcc_input.send_keys(bcc_string)
except Exception as e:
    print("Could not populate BCC input field:", e)


message = "Hello, Thanks for reaching out"

# Optional: fill in subject and message
driver.find_element(By.NAME, "subjectbox").send_keys("Test Subject")
driver.find_element(By.XPATH, "//div[@aria-label='Message Body']").send_keys(message)

# You can also click send if needed:
driver.find_element(By.XPATH, "//div[text()='Send']").click()
