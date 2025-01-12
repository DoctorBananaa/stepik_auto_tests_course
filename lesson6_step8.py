from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#link = 'http://suninjuly.github.io/registration1.html'
link = "http://suninjuly.github.io/registration2.html"
with webdriver.Chrome() as browser:
    browser.get(link)
    fields_placeholders = ['Input your first name', 'Input your last name', 'Input your email']
    [browser.find_element(By.CSS_SELECTOR, f'[placeholder="{placeholder}"]').send_keys("Ivan") for placeholder in fields_placeholders]
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
    time.sleep(10)