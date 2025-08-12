from selenium.webdriver.common.by import By


class OrderFeedPageLocators:

    PLACE_AN_ORDER = (By.XPATH,
                      "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")

    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")

    ORDER_HISTORY_BUTTON = (By.XPATH,
                            "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")

    ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")

    LAST_ORDER = (
        By.XPATH,
        "//body/div[@id='root']/div[@class='App_App__aOmNj']/main[@class='App_componentContainer__2JC2W']/div[@class='OrderFeed_orderFeed__2RO_j']/div[@class='OrderFeed_contentBox__3-tWb']/ul[@class='OrderFeed_list__OLh59']/li[1]/a[1]/div[1]"
    )

    ORDER_DETAILS_CONTENT = (
        By.XPATH,
        "//p[@class='text text_type_main-medium mb-8']"
    )

    TOTAL_ORDERS_COUNTER = (
        By.XPATH,
        "//div[@class='undefined mb-15']//p[contains(@class, 'OrderFeed_number__2MbrQ') and normalize-space(text())]"
    )

    TODAY_COMPLETED_COUNTER = (
        By.XPATH,
        "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"
    )

    CLOSE_ORDER_DETAILS_BUTTON = (By.XPATH, "//button[@type='button']//*[name()='svg']")

    ORDER_ID = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title') and normalize-space(text())]")

    ORDER_ID_IN_FEED = (By.XPATH, "//*[contains(text(), '{0}')]")

    ORDER_IN_PROGRESS_LOCATOR = (
        By.XPATH,
        "//ul[contains(@class, 'OrderFeed_orderList')]/li[1]"
    )

    FEED_TITLE = (
        By.XPATH,
        "//h1[contains(@class, 'text_type_main-large')]"
    )

    LOGIN_AFTER_LOGOUT_BURGER = (
    By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']")  # Локатор сразу после входа

    ORDER_PREPARING_MESSAGE = (By.XPATH, "//p[@class='undefined text text_type_main-small mb-2']") # Начали готовить

    ORDER_LOADING_MODAL = (
    By.XPATH, "//div[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//div[@class='Modal_modal_overlay__x2ZCr']")



