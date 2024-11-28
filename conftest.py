# файл для глобыльного хранилища фекстур



import pytest
from selene.support.shared import browser

@pytest.fixture(scope="session")  # module - файл, class - способ агрегации, session - выполнится на один запуск
def browser_open():
    print("Открытие браузера!")  # Здесь может быть код для инициализации браузера
    browser.open('https://google.com/ncr')

    yield

    print("Testing completed. Закрываем браузер!")  # Здесь может быть код для завершения работы браузера
    browser.quit()
