from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(chrome_options=co)

# 1) Wait 10 seconds until element is visible in page then returns element
def wait_for_element(selector_tuple, parent=driver, timeout=10, many=False):
    """
    Wait 10 seconds until element is visible in page then returns element
    selector_tuple: required and needs to be a tuple e.g. (By.ID, "some-id")
    """
    if many:
        selector = EC.presence_of_all_elements_located(selector_tuple)
    else:
        selector = EC.presence_of_element_located(selector_tuple)
    
    element = WebDriverWait(parent, timeout).until(selector)
    return element
    
# Example usage
