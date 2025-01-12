from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    #link = "http://suninjuly.github.io/registration1.html"
    # для второго теста ниже:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # Задание: " Проверьте, что можно зарегистрироваться на сайте, заполнив только обязательные поля, отмеченные символом *: First name, last name, email."
    # Соответственно проверка полей "First name, last name, email отмеченные символом *"
    l = ["First name", "Last name", "Email"]
    for t in l:
        z = "//div[*[contains(text(), " + "'" + t + "'" + ")]]/input"
        # Попытка обработать ошибку NoSuchElementException, без этого какие-то непонятные сообщения
        try:
            element = browser.find_element(By.XPATH, z)
            element.send_keys("z")
            # на звездочку уже забил, по-хорошему её тоже нужну было бы добавить, и проверить что элемент нашёлся один
            # наверно правильно запихать в массив elements и проверять что там один элемент, но поленился
        except Exception:
            print("видимо NoSuchElementException")
            break

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
