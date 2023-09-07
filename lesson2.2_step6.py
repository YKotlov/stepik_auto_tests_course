import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    browser = webdriver.Chrome()
    browser.get("https://SunInJuly.github.io/execute_script.html")
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)
    check_box = browser.find_element(By.CLASS_NAME, "form-check-input")
    check_box.click()
    radio_btn = browser.find_element(By.ID, "robotsRule")
    radio_btn.click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()