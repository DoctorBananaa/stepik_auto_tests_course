from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WebdriverLong(webdriver.Chrome):
    def __init__(self, link=None):
        super().__init__()
        if link:
            self.get(link)
        self.implicitly_wait(5)

    def __exit__(self, exc_type, exc_value, traceback):
        time.sleep(10)
        super().__exit__(exc_type, exc_value, traceback)

    def btn_click(self, rule, string):
        btn = self.find_element(rule, string)
        self.execute_script("return arguments[0].scrollIntoView(true);", btn)
        btn.click()