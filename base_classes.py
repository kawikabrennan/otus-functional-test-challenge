import unittest
from selenium import webdriver
from time import sleep


class BaseTestSetUp(unittest.TestCase):
    @classmethod
    def otus_login(cls, username, password):
        cls.driver.get(cls.otus_home_page)
        cls.driver.find_element_by_id(
            "otus-input-1").send_keys(username)
        cls.driver.find_element_by_id(
            "otus-input-3").send_keys(password)
        cls.driver.find_element_by_class_name("btn-login").click()

    @classmethod
    def setUpClass(cls):
        cls.enrolled_class = "QA Tech Challenge"
        cls.otus_home_page = "https://my.otus.com/"
        cls.otus_my_bookshelf = cls.otus_home_page + "bookshelf/my-bookshelf"
        cls.otus_my_classes = cls.otus_home_page + "classes/my-classes"
        cls.otus_lessons = cls.otus_home_page + "lesson"
        cls.otus_gradebook = cls.otus_home_page + "gradebook"
        cls.lesson_name = "QA Technical Challenge"
        cls.link_name = "Log In URL"
        cls.edited_link_name = r'   !@#$%^&*()-_=+`~[{]}\|;:,<.>/?  '
        cls.assessments_table_xpath = (
            "//*[@id='outerWrapper']/otus-app/ot-theme-provider/main/div/div/ng-component/"
            "ng-component/ot-assess-list-student/div/div[2]/table/tbody/tr"
        )

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        cls.driver = webdriver.Chrome()  # (chrome_options=options)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        sleep(3)
        cls.driver.close()
