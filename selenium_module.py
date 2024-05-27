import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class SeleniumModule:
    def __init__(self, driver_path, base_url, wait_time):
        self.driver_path = driver_path
        self.base_url = base_url
        self.wait_time = wait_time
        self.driver = None

    def setup_driver(self):
        service = Service(self.driver_path)
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()

    def navigate_to_page(self):
        self.driver.get(self.base_url)
        time.sleep(self.wait_time)

    def check_element_css_properties(self, locator, properties):
        wait = WebDriverWait(self.driver, self.wait_time)
        element = wait.until(EC.presence_of_element_located(locator))
        for prop, expected_value in properties.items():
            actual_value = element.value_of_css_property(prop)
            assert actual_value == expected_value, f"Test {prop} fail: expected {expected_value}, got {actual_value}"

    def teardown(self):
        self.driver.quit()
