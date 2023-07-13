from locators.locators import SimplePageLocators
from pages.basepage import BasePage


class SimplePage(BasePage):
    locators = SimplePageLocators()

    def check_buttons(self):
        self.element_is_visible(self.locators.ELEMENTS).click()
        self.element_is_visible(self.locators.BUTTONS).click()
        button = self.element_is_visible(self.locators.DOUBLE_CLICK)
        self.action_right_click(button)
        message = self.element_is_present(self.locators.MESSAGE).text
        print(message)
        return message
