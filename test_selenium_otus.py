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
        self.driver.find_element_by_class_name("btn-login").click()

    def tearDown(self):
        sleep(3)
        self.driver.close()


class UnenrolledTests(BaseSetUp, unittest.TestCase):
    def __init__(self, methodName="runTest"):
        unittest.TestCase.__init__(self, methodName)
        BaseSetUp.__init__(self, USERDEFAULT, PASSDEFAULT)

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
        self.driver.find_element_by_xpath(
            "//a/span[.='Bookshelf']").click()
        self.driver.find_element_by_xpath(
            "//a/span[.='My Bookshelf']").click()
        self.driver.find_element_by_xpath(
            "//button/span/ot-icon[@name='plus']").click()

        # self.assertEqual(len(assessments_table), 0)


# class EnrolledTests(BaseSetUp, unittest.TestCase):
#     def __init__(self, methodName="runTest"):
#         unittest.TestCase.__init__(self, methodName)
#         BaseSetUp.__init__(self, USERENROLLED, PASSENROLLED)

#     def test_assessments_available(self):
#         """The Assessments table is empty."""
#         self.driver.find_element_by_xpath(
#             "//a/span[.='Assessments']").click()
#         assessments_table = self.driver.find_elements_by_xpath(
#             "//table/tbody/*"
#         )
#         self.assertEqual(len(assessments_table), 1)


if __name__ == "__main__":
    unittest.main()
