from click_and_with import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

with WebdriverLong('http://suninjuly.github.io/explicit_wait2.html') as browser:
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    browser.btn_click(By.ID, 'book')

    x_value = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(str(math.log(abs(12 * math.sin(int(x_value))))))
    browser.btn_click(By.ID, 'solve')