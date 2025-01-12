from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time

class WebdriverLong(webdriver.Chrome):
    def __exit__(self, exc_type, exc_value, traceback):
        time.sleep(10)
        super().__exit__(exc_type, exc_value, traceback)

def btn_click(rule, string):
    browser.find_element(rule, string).click()

with WebdriverLong() as browser:
    browser.get('https://suninjuly.github.io/get_attribute.html')
    x_element = browser.find_element(By.ID, 'treasure').get_attribute("valuex")

    input_place = browser.find_element(By.ID, 'answer')
    input_place.send_keys(str(math.log(abs(12*math.sin(int(x_element))))))

    btns = [
        (By.ID, "robotCheckbox"),
        (By.ID, "robotsRule"),
        (By.CLASS_NAME, "btn-default")
    ]

    [btn_click(*btn) for btn in btns]