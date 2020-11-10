import unittest
from credentials import USERDEFAULT, PASSDEFAULT
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from helper import wait_class_name_loads


class UnenrolledTests(unittest.TestCase):
    @classmethod
    def otus_login(cls):
        cls.driver.get(cls.otus_home_page)
        cls.driver.find_element_by_id(
            "otus-input-1").send_keys(USERDEFAULT)
        cls.driver.find_element_by_id(
            "otus-input-3").send_keys(PASSDEFAULT)
        cls.driver.find_element_by_class_name("btn-login").click()

    @classmethod
    def setUpClass(cls):
        cls.otus_home_page = "https://my.otus.com/"
        cls.otus_my_bookshelf = cls.otus_home_page + "bookshelf/my-bookshelf"

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        cls.driver = webdriver.Chrome()  # (chrome_options=options)
        cls.driver.implicitly_wait(10)
        cls.otus_login()

    @classmethod
    def tearDownClass(cls):
        sleep(3)
        cls.driver.close()

    def test_assessments_none_available(self):
        """The Assessments table is empty."""
        self.driver.find_element_by_xpath(
            "//a/span[.='Assessments']").click()

        wait_class_name_loads(self.driver, 10, "otus-large-table")

        assessments_table = self.driver.find_elements_by_xpath(
            "//table/tbody/*"
        )

        self.assertEqual(len(assessments_table), 0)

    def test_bookshelf_add_link(self):
        """A link is added to the resource table."""
        link_name = "Log In URL"

        # TODO: Work on hover action instead of going directly to the page
        # element_to_hover_over = self.driver.find_element_by_xpath(
        #     "//ot-student-navbar/div/div")
        # hover = ActionChains(self.driver).move_to_element(
        #     element_to_hover_over)
        # hover.perform()

        self.driver.get(self.otus_my_bookshelf)
        self.driver.find_element_by_xpath(
            "//button[@aria-label='open actions menu']").click()

        menu_items = self.driver.find_elements_by_class_name(
            "ot-option-container")
        menu_items[0].click()

        self.driver.find_element_by_xpath(
            "//div/span[.='Link']").click()

        wait_class_name_loads(self.driver, 10, "otus-new-modal__wrapper")

        text_fields = self.driver.find_elements_by_xpath(
            "//div[@class='otus-new-modal__wrapper']//input[@type='text']")
        text_fields[0].send_keys(self.otus_home_page)
        text_fields[1].send_keys(link_name)

        self.driver.find_element_by_xpath(
            "//button/span[contains(.,'Save')]").click()

        created_link = self.driver.find_element_by_xpath(
            f'//table//span[.="{link_name}"]')

        self.assertTrue(created_link)


if __name__ == "__main__":
    unittest.main()
