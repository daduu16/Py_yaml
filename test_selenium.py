import pytest

def test_elements(selenium_module, element_properties):
    selenium_module.navigate_to_page()

    for element_name, properties in element_properties.items():
        locator = properties["locator"]
        css_properties = properties["properties"]
        selenium_module.check_element_css_properties(locator, css_properties)
