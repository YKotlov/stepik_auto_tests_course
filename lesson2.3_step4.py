import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    browser.switch_to.alert.accept()
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    time.sleep(10)
    browser.quit()
