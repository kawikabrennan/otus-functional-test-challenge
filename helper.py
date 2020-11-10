from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_class_name_loads(driver, seconds: int, class_name: str):
    WebDriverWait(driver, seconds).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, class_name))
    )
