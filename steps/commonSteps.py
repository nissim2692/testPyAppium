import time

from appium.webdriver.common.touch_action import TouchAction
from behave import given, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(u'launch application')
def step_impl(context):
    wait = WebDriverWait(context.browser, 10)
    wait.until(EC.visibility_of_element_located((By.ID, 'skip_sign_in_button')))
    context.browser.find_element_by_id("skip_sign_in_button").click()


@then(u'user scrolls down the page on app')
def scroll_down(context):

    size = context.browser.get_window_rect()
    x = (size['width'] * 0.5)
    y1 = (size['height'] * 0.5)
    y2 = (size['height'] * 0.01)

    actions = TouchAction(context.browser)
    actions.press(el=None, x=x, y=y1, pressure=None).move_to(el=None, x=x, y=y2).release().perform()
    actions.press(el=None, x=x, y=y1, pressure=None).move_to(el=None, x=x, y=y2).release().perform()


    time.sleep(5)
    print("Scroll down completed")


@then(u'user scrolls up the page on app')
def scroll_up(context):

    size = context.browser.get_window_rect()
    x = (size['width'] * 0.5)
    y1 = (size['height'] * 0.5)
    y2 = (size['height'] * 0.2)

    actions = TouchAction(context.browser)
    actions.press(el=None, x=x, y=y2, pressure=None).move_to(el=None, x=x, y=y1).release().perform()
    actions.press(el=None, x=x, y=y2, pressure=None).move_to(el=None, x=x, y=y1).release().perform()


    time.sleep(5)
    print("Scroll up completed")
