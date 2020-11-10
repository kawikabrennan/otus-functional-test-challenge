import unittest
from credentials import USERDEFAULT, PASSDEFAULT
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep


class UnenrolledTests(unittest.TestCase):
    @classmethod
    def otus_login(cls):
        cls.driver.get("https://my.otus.com/")
        cls.driver.find_element_by_id(
            "otus-input-1").send_keys(USERDEFAULT)
        cls.driver.find_element_by_id(
            "otus-input-3").send_keys(PASSDEFAULT)
        cls.driver.find_element_by_class_name("btn-login").click()

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        cls.driver = webdriver.Chrome()  # (chrome_options=options)
        cls.driver.implicitly_wait(10)
        cls.otus_login()

    @classmethod
    def tearDownClass(cls):
        # sleep(3)
        cls.driver.close()

    def test_assessments_none_available(self):
        """The Assessments table is empty."""
        self.driver.find_element_by_xpath(
            "//a/span[.='Assessments']").click()
        assessments_table = self.driver.find_elements_by_xpath(
            "//table/tbody/*"
        )

        self.assertEqual(len(assessments_table), 0)

    def test_bookshelf_add_link(self):
        """A link is added to the resource table."""

        # element_to_hover_over = self.driver.find_element_by_xpath(
        #     "//ot-student-navbar/div/div")
        # hover = ActionChains(self.driver).move_to_element(
        #     element_to_hover_over)
        # hover.perform()

        self.driver.get("https://my.otus.com/bookshelf/my-bookshelf")
        self.driver.find_element_by_xpath(
            "//button[@aria-label='open actions menu']").click()

        # self.assertEqual(len(assessments_table), 0)


if __name__ == "__main__":
    unittest.main()
