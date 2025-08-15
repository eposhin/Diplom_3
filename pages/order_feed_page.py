import allure
from .base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from data.data import FEED_URL


class OrderFeedPage(BasePage):

    @allure.step('Кликнуть на последний заказ в ленте')
    def click_last_order(self):
        self.click_to_element(OrderFeedPageLocators.LAST_ORDER)

    @allure.step('Получить содержимое деталей заказа')
    def get_order_details_content(self):
        return self.get_text_from_element(OrderFeedPageLocators.ORDER_DETAILS_CONTENT)

    @allure.step('Получить общее количество заказов')
    def get_total_orders_counter(self):
        return int(self.get_text_from_element(OrderFeedPageLocators.TOTAL_ORDERS_COUNTER))

    @allure.step('Получить количество выполненных заказов за сегодня')
    def get_today_completed_counter(self):

        element = self.find_element_with_wait(OrderFeedPageLocators.TODAY_COMPLETED_COUNTER)
        return int(element.text.strip())

    @allure.step('Открыть страницу ленты заказов')
    def open_feed_page(self):
        self.navigate_to(FEED_URL)
        self.wait_for_element_visible(OrderFeedPageLocators.FEED_TITLE)

    @allure.step('Кликнуть кнопку Конструктор')
    def click_constructor(self):
        self.click_to_element(OrderFeedPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Кликнуть кнопку Лента заказов')
    def click_feed(self):
        self.wait_for_element_visible(OrderFeedPageLocators.LOGIN_AFTER_LOGOUT_BURGER)
        self.click_when_clickable(OrderFeedPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Кликнуть кнопку Оформить заказ')
    def click_place_an_order(self):
        self.click_to_element(OrderFeedPageLocators.PLACE_AN_ORDER)

    @allure.step('Закрыть окно деталей заказа')
    def click_close_order_details(self):
        self.click_when_clickable(OrderFeedPageLocators.CLOSE_ORDER_DETAILS_BUTTON)

    @allure.step('Получить номер заказа из деталей')
    def get_order_id_from_details(self):
        self.find_and_wait_until_text_changes(OrderFeedPageLocators.ORDER_ID, "9999")
        return self.get_text_from_element(OrderFeedPageLocators.ORDER_ID)

    @allure.step('Проверить наличие номера заказа в ленте')
    def is_order_id_in_feed(self, order_id):
        formatted_id = f"{int(order_id):07d}"
        order_locator = OrderFeedPageLocators.ORDER_ID_IN_FEED
        order_locator = (order_locator[0], order_locator[1].format(formatted_id))
        return self.find_element_with_wait(order_locator)

    @allure.step('Проверить что заказ в процессе выполнения')
    def is_order_number_in_progress(self, order_id):
        formatted_id = f"{int(order_id):07d}"
        self.find_and_format_locator(OrderFeedPageLocators.ORDER_IN_PROGRESS_LOCATOR, formatted_id)
        return True