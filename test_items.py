import time
from selenium.webdriver.common.by import By

def test_add_to_basket_button(browser):
    # Открытие страницы товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Задержка для проверки отображения страницы на разных языках
    time.sleep(30)

    # Поиск кнопки добавления в корзину
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR,
                                                "button.btn-add-to-basket")

    # Проверка, что кнопка присутствует на странице
    assert add_to_basket_button is not None, "Button 'Add to basket' not found"
