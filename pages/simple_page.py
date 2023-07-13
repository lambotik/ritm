from ritm.locators.locators import SimplePageLocators
from ritm.pages.basepage import BasePage


class SimplePage(BasePage):
    locators = SimplePageLocators()

    def check_result_click(self, output):
        print('Output Message: ', self.element_is_present(output).text)
        return self.element_is_present(output).text

    def check_buttons(self):
        self.element_is_visible(self.locators.ELEMENTS).click()
        self.element_is_visible(self.locators.BUTTONS).click()
        button = self.element_is_visible(self.locators.DOUBLE_CLICK)
        self.action_right_click(button)
        message = self.element_is_present(self.locators.MESSAGE).text
        print(message)
        return message






