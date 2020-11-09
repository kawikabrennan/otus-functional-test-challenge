import unittest
from credentials import USERENROLLED, PASSENROLLED, USERDEFAULT, PASSDEFAULT
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class BaseSetUp(unittest.TestCase):
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome()  # (chrome_options=options)
        self.driver.implicitly_wait(10)
        self.otus_login()

    def otus_login(self):
        self.driver.get("https://my.otus.com/")
        self.driver.find_element_by_id(
            "otus-input-1").send_keys(self.user)
        self.driver.find_element_by_id(
            "otus-input-3").send_keys(self.password)
        buttons = self.driver.find_elements_by_class_name("btn-login")
        buttons[0].click()

    def tearDown(self):
        sleep(5)
        self.driver.close()


class UnenrolledTests(BaseSetUp, unittest.TestCase):
    def __init__(self, methodName="runTest"):
        unittest.TestCase.__init__(self, methodName)
        BaseSetUp.__init__(self, USERDEFAULT, PASSDEFAULT)

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
        self.assertTrue(5 == 5)


if __name__ == "__main__":
    unittest.main()
