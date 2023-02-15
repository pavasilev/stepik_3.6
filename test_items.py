from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_presence_of_a_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    browser.implicitly_wait(5)
    item = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert item, 'Button doesnt exist'
