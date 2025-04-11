import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')
time.sleep(10)

keys = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]
bodyhtml = browser.find_element(By.TAG_NAME, 'body')
continue_game = True
while continue_game:
    move = random.randint(0,3)
    bodyhtml.send_keys(keys[move])
    time.sleep(0.2)
    try:
        game_over_html = browser.find_elements(By.TAG_NAME, 'button')
        for game_over in game_over_html:
            if game_over.text == 'Play Again':
                print('Game Over')
                continue_game = False
                break
    except Exception as e:
        continue
print("Done")
time.sleep(10)
browser.quit()
