from selenium.webdriver.common.by import By
import time

def test_different_languages(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(10)
    assert browser.find_element(By.CLASS_NAME, 'btn-add-to-basket'), 'Кнопки добавления в корзину нет'