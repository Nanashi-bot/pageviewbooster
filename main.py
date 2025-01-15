from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get("https://github.com/Nanashi-bot")

try:
    while True:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))  # Waiting for body tag to load
        )
        sleep(0.5)  # Increase this value to wait for some time before page refreshes to avoid rate limiting
        driver.refresh()  # refresh the page
except KeyboardInterrupt:
    print("Refreshing stopped.")
    driver.quit()

