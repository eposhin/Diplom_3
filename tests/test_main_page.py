import allure
from data.data import EMAIL, PASSWORD
from pages.main_page import MainPage
from pages.account_page import AccountPage


@allure.feature('Основной функционал')
@allure.story('Тесты функционала главной страницы')
class TestMainPage:

    @allure.title('Тест переход по клику на «Конструктор»')
    def test_click_constructor(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открываем страницу входа'):
            account_page.open_login_page()

        with allure.step('Нажимаем на "Конструктор"'):
            main_page.click_constructor()

        with allure.step('Проверяем, что секция "Собери бургер" отображается'):
            assert main_page.is_burger_constructor_visible(), "Секция 'Собери бургер' не отображается!"

    @allure.title('Тест переход по клику на раздел «Лента заказов»')
    def test_click_order_feed(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открываем страницу входа'):
            account_page.open_login_page()

        with allure.step('Нажимаем на "Лента заказов"'):
            main_page.click_order_feed()

        with allure.step('Проверяем, что счетчик выполненных заказов отображается'):
            assert main_page.is_order_feed_counter_visible(), "Счетчик выполненных заказов не отображается!"

    @allure.title('Тест если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открываем страницу входа'):
            account_page.open_login_page()

        with allure.step('Нажимаем на "Конструктор"'):
            main_page.click_constructor()

        with allure.step('Нажимаем на ингредиент'):
            main_page.click_ingredient()

        with allure.step('Проверяем, что окно с деталями ингредиента отображается'):
            assert main_page.is_ingredient_details_visible(), "Детали ингредиента не отображаются!"

    @allure.title('Тест всплывающее окно закрывается кликом по крестику')
    def test_close_details(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открываем страницу входа'):
            account_page.open_login_page()

        with allure.step('Нажимаем на "Конструктор"'):
            main_page.click_constructor()

        with allure.step('Нажимаем на ингредиент'):
            main_page.click_ingredient()

        with allure.step('Закрываем окно с деталями ингредиента'):
            main_page.close_ingredient_details()

        with allure.step('Проверяем, что окно с деталями ингредиента закрыто'):
            assert not main_page.is_ingredient_details_visible()

    @allure.title('Тест при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открываем страницу входа'):
            account_page.open_login_page()

        with allure.step('Нажимаем на "Конструктор"'):
            main_page.click_constructor()

        with allure.step('Получаем начальное значение счетчик ингредиентов'):
            initial_counter = main_page.get_ingredient_counter()

        with allure.step('Добавляем ингредиент в заказ'):
            main_page.put_ingredient_into_basket()

        with allure.step('Проверяем, что счетчик увеличился'):
            updated_counter = main_page.get_ingredient_counter()

        assert updated_counter == initial_counter + 2, \
            f"Счетчик не увеличился! Ожидалось: {initial_counter + 2}, но получено: {updated_counter}"
