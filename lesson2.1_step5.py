import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    check_box = browser.find_element(By.CLASS_NAME, "form-check-input")
    check_box.click()
    radio_btn = browser.find_element(By.ID, "robotsRule")
    radio_btn.click()
    submit_btn = browser.find_element(By.CLASS_NAME, "btn btn-default")
    submit_btn.click()
finally:
    time.sleep(30)
    browser.quit()
