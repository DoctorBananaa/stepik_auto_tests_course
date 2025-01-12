from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"
with webdriver.Chrome() as browser:
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    input_place = browser.find_element(By.ID, 'answer')
    input_place.send_keys(y)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    submit = browser.find_element(By.CLASS_NAME, "btn-default")
    submit.click()
    time.sleep(10)