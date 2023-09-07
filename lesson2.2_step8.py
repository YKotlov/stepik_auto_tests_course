import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    name = browser.find_element(By.NAME, "firstname")
    name.send_keys("Александр")
    lastname = browser.find_element(By.NAME, "lastname")
    lastname.send_keys("Волжский")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("abcde@ui.dot")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'abc.txt')
    element = browser.find_element(By.NAME, "file")
    element.send_keys(file_path)
    btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    btn.click()
finally:
    time.sleep(10)
    browser.quit()
