from click_and_with import *

with WebdriverLong('http://suninjuly.github.io/cats.html') as browser:
    browser.find_element(By.ID, "button")