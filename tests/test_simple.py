from ritm.pages.simple_page import SimplePage


class TestSimple:
    def test_elements(self, driver):
        test_elements = SimplePage(driver, 'https://demoqa.com/')
        test_elements.open()
        text = test_elements.check_buttons()
        assert text == 'You have done a right click'

