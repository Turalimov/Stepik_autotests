class MainPage(self, browser):
    SEARCH_BAR = browser.find_element('xpath', "//input[@name='q']")
    SEARCH_BTN = browser.find_element('xpath', "//input[@value='Search']")

    def click_on_search_bar(self):
        self.SEARCH_BAR.click()

    def input_value_to_searchbar(self, value):
        self.SEARCH_BAR.send_keys(value)

    def click_on_search_button(self):
        self.SEARCH_BTN.click()
