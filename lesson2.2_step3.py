import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")
    n1 = browser.find_element(By.ID, "num1")
    N1 = n1.text
    n2 = browser.find_element(By.ID, "num2")
    N2 = n2.text
    calc = (int(N1) + int(N2))
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(calc))
    sbmt = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    sbmt.click()
finally:
    time.sleep(10)
    browser.quit()