from click_and_with import *
import math

with WebdriverLong('https://suninjuly.github.io/execute_script.html') as browser:
    x_element = browser.find_element(By.ID, 'input_value').text
    input_place = browser.find_element(By.ID, 'answer')
    input_place.send_keys(str(math.log(abs(12 * math.sin(int(x_element))))))

    btns = [
        (By.ID, "robotCheckbox"),
        (By.ID, "robotsRule"),
        (By.CLASS_NAME, "btn-primary")
    ]

    [browser.btn_click(*btn) for btn in btns]