import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop

class MainPage(BasePage):
    @allure.step('Нажать кнопку Конструктор')
    def click_constructor(self):
        self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Нажать кнопку Оформить заказ')
    def click_place_an_order(self):
        self.click_to_element(MainPageLocators.PLACE_AN_ORDER)

    @allure.step('Проверить видимость раздела конструктора бургеров')
    def is_burger_constructor_visible(self):
        return self.find_element_with_wait(MainPageLocators.BURGER_CONSTRUCTOR_SECTION).is_displayed()

    @allure.step('Нажать кнопку Лента заказов')
    def click_order_feed(self):
        self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Проверить видимость счетчика выполненных заказов')
    def is_order_feed_counter_visible(self):
        return self.find_element_with_wait(MainPageLocators.COMPLETED_ORDERS).is_displayed()

    @allure.step('Выбрать ингредиент')
    def click_ingredient(self):
        self.click_to_element(MainPageLocators.INGREDIENT_R2D3_BUN)

    @allure.step('Проверить видимость деталей ингредиента')
    def is_ingredient_details_visible(self):
        return self.is_element_displayed(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)

    @allure.step('Закрыть окно деталей ингредиента')
    def close_ingredient_details(self):
        self.click_to_element(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)

    @allure.step('Получить счетчик ингредиента')
    def get_ingredient_counter(self):
        return int(self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER))

    @allure.step('Перетащить ингредиент в конструктор')
    def drag_and_drop_ingredient(self):
        ingredient_locator = MainPageLocators.INGREDIENT_R2D3_BUN
        target_locator = MainPageLocators.ORDER_TARGET_TOP
        self.drag_and_drop(ingredient_locator, target_locator)

    @allure.step('Добавить ингредиент в корзину')
    def put_ingredient_into_basket(self):
        self.main_page_loading_wait()
        ingredient = self.find_element_with_wait(locator=MainPageLocators.INGREDIENT_R2D3_BUN)
        basket = self.find_element_with_wait(locator=MainPageLocators.ORDER_TARGET_TOP)
        self.drag_and_drop_element(source=ingredient, target=basket)

    @allure.step('Получить сообщение об успешном заказе')
    def get_order_success_message(self):
        return self.get_text_from_element(MainPageLocators.ORDER_SUCCESS_MESSAGE)

    @allure.step('Ожидание загрузки главной страницы')
    def main_page_loading_wait(self):
        self.wait_for_element_visible(MainPageLocators.MAIN_PAGE_MARKER)