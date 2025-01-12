from click_and_with import *
import math

with WebdriverLong('https://suninjuly.github.io/alert_accept.html') as browser:
    browser.btn_click(By.TAG_NAME, 'button')
    browser.switch_to.alert.accept()
    time.sleep(1)

    x_value = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(str(math.log(abs(12 * math.sin(int(x_value))))))
    browser.btn_click(By.TAG_NAME, 'button')