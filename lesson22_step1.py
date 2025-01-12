from click_and_with import *
from selenium.webdriver.support.ui import Select

with WebdriverLong('https://suninjuly.github.io/selects1.html') as browser:
    num1, num2 = browser.find_element(By.ID, 'num1'), browser.find_element(By.ID, 'num2')

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(int(num1.text) + int(num2.text)))

    browser.btn_click(By.CLASS_NAME, 'btn-default')