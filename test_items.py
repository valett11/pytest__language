from time import sleep
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_cart_button(browser):
    browser.get(link)
    item = browser.find_elements(By.CSS_SELECTOR,"#add_to_basket_form button")
    sleep(5)
    assert item, 'no item'
