import pytest
import yaml
from selenium_module import SeleniumModule

@pytest.fixture(scope="session")
def config():
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)

@pytest.fixture(scope="session")
def selenium_module(config):
    module = SeleniumModule(
        driver_path=config["driver_path"],
        base_url=config["base_url"],
        wait_time=config["wait_time"]
    )
    module.setup_driver()
    yield module
    module.teardown()

@pytest.fixture(scope="session")
def element_properties():
    return {
        "logo_icon": {
            "locator": (By.CSS_SELECTOR, 'div.logo__icon'),
            "properties": {
                "width": "300px",
                "height": "175px"
            }
        },
        "login_form": {
            "locator": (By.CSS_SELECTOR, 'div.login-form'),
            "properties": {
                "background-color": "rgba(0, 0, 0, 0)"
            }
        },
        "password_div": {
            "locator": (By.CSS_SELECTOR, 'div[form] div:nth-child(1) > div:nth-child(2)'),
            "properties": {
                "width": "372px",
                "height": "40px"
            }
        },
        "email_div": {
            "locator": (By.CSS_SELECTOR, 'div[form] div:nth-child(1) > div:nth-child(3) > div:nth-child(1)'),
            "properties": {
                "width": "133.688px",
                "height": "40px"
            }
        },
        "domain_div": {
            "locator": (By.CSS_SELECTOR, 'div[form] div:nth-child(1) > div:nth-child(3) > div:nth-child(3)'),
            "properties": {
                "width": "133.688px",
                "height": "40px"
            }
        },
        "next_button": {
            "locator": (By.CSS_SELECTOR, 'div[form] div:nth-child(2) > a'),
            "properties": {
                "font-family": "sans-serif",
                "font-size": "14.4px"
            }
        }
    }
