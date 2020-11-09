import unittest
from credentials import USERENROLLED, PASSENROLLED, USERDEFAULT, PASSDEFAULT
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class UnenrolledTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome()  # (chrome_options=options)
        self.driver.implicitly_wait(10)

    @unittest.skip("skipping tutorial test")
    def test_search_in_python_org(self):
        self.driver.get("http://www.python.org")
        assert "Python" in self.driver.title
        elem = self.driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in self.driver.page_source

    def test_open_myotus(self):
        self.driver.get("https://my.otus.com/")
        email_element = self.driver.find_element_by_id(
            "otus-input-1").send_keys(USERDEFAULT)
        input_element = self.driver.find_element_by_id(
            "otus-input-3").send_keys(PASSDEFAULT)
        buttons = self.driver.find_elements_by_class_name("btn-login")
        print(buttons[0].click())

    def tearDown(self):
        sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
