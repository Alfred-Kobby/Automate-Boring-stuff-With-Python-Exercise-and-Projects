import os
import bs4
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.flickr.com/'
os.makedirs('downloads', exist_ok=True)

search_word = input('Enter word to search: ')

browser = webdriver.Firefox()
browser.get(url)

search = browser.find_element(By.ID, 'text-2')
search.send_keys(search_word)
search.submit()

WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "overlay")))

images_link = browser.find_elements(By.CLASS_NAME, 'overlay')
print(f'length: {len(images_link)}')
for i in range(len(images_link)):
    link = requests.get(images_link[i].get_attribute('href'))
    link.raise_for_status()
    image_url = bs4.BeautifulSoup(link.text, 'html.parser')
    img = image_url.select('.main-photo')
    if not img:
        print('No image found')
    else:
        try:
            img_url = 'https:' + img[0].get('src')
            res = requests.get(img_url)
            res.raise_for_status()
        except Exception as e:
            print("could not process: " + img[0].get('src'))

        print('Downloading image %s...' % img_url)
        imageFile = open(os.path.join('downloads', os.path.basename(img_url)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
print("Done")
browser.quit()
