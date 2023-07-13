from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.timeout = 5

    def open(self):
        """
        This function open received URL.

        open: str(link)
        """
        self.driver.get(self.url)

    def get_current_url(self):
        """
        This function return current URL
        :return: link(url)
        """
        get_url = self.url
        return get_url

    def element_is_present(self, locator):
        return wait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

    def element_is_visible(self, locator):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))

    def go_to_element(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element).perform()

