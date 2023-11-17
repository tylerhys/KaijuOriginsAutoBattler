from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9515")

s = Service('C:/Program Files (x86)/Google/Chrome/Application/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)

window_handles = driver.window_handles
print(window_handles)

driver.switch_to.window(window_handles[0])
page = driver.find_element(By.TAG_NAME, 'body')
runs = 0

# Bot Loop
while True:
    i = 0
    while i < 12:
        page.send_keys("E")
        time.sleep(0.1)
        i += 1

    wait = WebDriverWait(driver, 60)
    find_ok = wait.until(EC.presence_of_element_located((By.XPATH, "//img[contains(@src, 'assets/sprites/help/ok-button-idle.webp')]")))
    ok = driver.find_element(By.XPATH,value="//img[contains(@src, 'assets/sprites/help/ok-button-idle.webp')]")
    ok.click()
    time.sleep(0.2)
    page.send_keys("E")
    page.send_keys("E")
    page.send_keys("E")
    page.send_keys("E")
    time.sleep(0.2)
    runs += 1
    print(f"Total Runs Completed: {runs}")

