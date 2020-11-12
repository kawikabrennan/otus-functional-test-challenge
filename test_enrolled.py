import unittest
from credentials import USERENROLLED, PASSENROLLED
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep
from base_classes import BaseTestSetUp


class EnrolledTests(BaseTestSetUp):
    @classmethod
    def setUpClass(cls):
        super(EnrolledTests, cls).setUpClass()
        cls.otus_login(USERENROLLED, PASSENROLLED)

    def test_assessments_available(self):
        """The Assessments table has one assessment. TODO: Investigate why the actual result is sometimes 0."""
        self.driver.find_element_by_xpath(
            "//a/span[.='Assessments']").click()
        assessments_table = self.driver.find_elements_by_xpath(
            self.assessments_table_xpath)
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
        """The Lessons page has one lesson."""
        self.driver.get(self.otus_lessons)

        lessons_table = self.driver.find_elements_by_xpath(
            "//table/tbody/*"
        )
        self.assertEqual(len(lessons_table), 1)
        self.assertTrue(self.lesson_name in lessons_table[0].text)

    def test_lessons_can_be_viewed(self):
        """The lesson is selectable and loads a new page."""
        lessons_table = self.driver.find_elements_by_xpath(
            "//table/tbody/*"
        )
        lessons_table[0].click()

        lesson_cards = self.driver.find_elements_by_xpath(
            "//lesson-card"
        )

        self.assertEqual(len(lesson_cards), 3)

    def test_otus_grades_available(self):
        """The Gradebook page is not empty."""
        self.driver.get(self.otus_gradebook)
        contents = True

        try:
            self.driver.find_element_by_xpath(
                "//*[@id='gradebook-page']"
            )
        except NoSuchElementException:
            contents = False
        self.assertTrue(contents)

    def test_otus_grades_click_shows_analytics(self):
        """Selecting the row that appears in the Gradebook make an analytics table appear."""
        sleep(2)

        self.driver.find_element_by_xpath(
            "//*[@id='gradebook-container']/ot-student-family-gradebook/div/div[3]/"
            "ot-student-gradebook-grid/div/ui-grid-action/div/div/div[1]/ag-grid-angular/"
            "div/div[1]/div/div[3]/div[1]/div/div/div"
        ).click()

        grade_details = self.driver.find_element_by_xpath(
            "//*[@id='gradebook-container']/ot-student-family-gradebook/div/div[3]/ot-student-gradebook-grid/div/div"
        )

        self.assertTrue(grade_details)


if __name__ == "__main__":
    unittest.main()
