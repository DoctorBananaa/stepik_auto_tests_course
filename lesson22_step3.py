from click_and_with import *
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

with WebdriverLong('https://suninjuly.github.io/file_input.html') as browser:
    fields = browser.find_elements(By.CLASS_NAME, 'form-control')
    [field.send_keys('abc') for field in fields]

    file_input = browser.find_element(By.ID, 'file')
    file_input.send_keys(file_path)

    browser.btn_click(By.CLASS_NAME, 'btn-primary')