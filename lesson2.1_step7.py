import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/get_attribute.html")
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    chest = browser.find_element(By.ID, "treasure")
    x_element = chest.get_attribute("valuex")
    x = x_element
    y = calc(x)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    check_box = browser.find_element(By.ID, "robotCheckbox")
    check_box.click()
    radio_btn = browser.find_element(By.ID, "robotsRule")
    radio_btn.click()
    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_btn.click()
finally:
    time.sleep(30)
    browser.quit()
