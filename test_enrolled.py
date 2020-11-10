import unittest
from credentials import USERENROLLED, PASSENROLLED
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class EnrolledTests(unittest.TestCase):
    @classmethod
    def otus_login(cls):
        cls.driver.get(cls.otus_home_page)
        cls.driver.find_element_by_id(
            "otus-input-1").send_keys(USERENROLLED)
        cls.driver.find_element_by_id(
            "otus-input-3").send_keys(PASSENROLLED)
        cls.driver.find_element_by_class_name("btn-login").click()

    @classmethod
    def setUpClass(cls):
        cls.enrolled_class = "QA Tech Challenge"
        cls.otus_home_page = "https://my.otus.com/"
        cls.otus_my_classes = cls.otus_home_page + "classes/my-classes"
        cls.otus_lessons = cls.otus_home_page + "lesson"

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        cls.driver = webdriver.Chrome()  # (chrome_options=options)
        cls.driver.implicitly_wait(10)
        cls.otus_login()

    @classmethod
    def tearDownClass(cls):
        sleep(3)
        cls.driver.close()

    def test_assessments_available(self):
        """The Assessments table has one assessment."""
        self.driver.find_element_by_xpath(
            "//a/span[.='Assessments']").click()
        assessments_table = self.driver.find_elements_by_xpath(
            "//table/tbody/*"
        )
        self.assertEqual(len(assessments_table), 1)

    def test_classes_available(self):
        """The Classes page has one class."""
        self.driver.get(self.otus_my_classes)

        classes = self.driver.find_elements_by_xpath(
            "//div[@class='class-card']"
        )

        current_class = classes[0].find_element_by_xpath(
            ".//div[@class='class-card__title']/span")

        self.assertEqual(len(classes), 1)
        self.assertEqual(self.enrolled_class, current_class.text)

    def test_lessons_available(self):
        """The Lessons page is empty. TODO: Learn to check the notification"""
        self.driver.get(self.otus_lessons)

        lessons_table = self.driver.find_elements_by_xpath(
            "//table/tbody/*"
        )
        self.assertEqual(len(lessons_table), 1)


if __name__ == "__main__":
    unittest.main()
