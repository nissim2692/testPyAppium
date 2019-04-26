import re
import time

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from steps.commonSteps import step_check_sorting


@then(u'user clicks on "{sub_category}" sub-category')
def step_select_category(context, sub_category):
    wait = WebDriverWait(context.browser, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@content-desc=\"" + sub_category + "\"]")))
    context.browser.find_element_by_xpath("//*[@content-desc=\"" + sub_category + "\"]").click()

    wait.until(
        EC.invisibility_of_element_located((By.XPATH, "//android.view.View[@content-desc=\"" + sub_category + "\"]")))


@then(u'user clicks on element with description "{element_description}" from result set')
def step_select_element_by_accessibility(context, element_description):
    wait = WebDriverWait(context.browser, 50)
    wait.until(EC.visibility_of_element_located((MobileBy.ACCESSIBILITY_ID, element_description)))
    context.browser.find_element_by_accessibility_id(element_description).click()
    wait.until(EC.invisibility_of_element_located((MobileBy.ACCESSIBILITY_ID, element_description)))


@then(u'validate elements in list view for sub-category {sub_category_value}')
def step_validate_sub_category_elements(context, sub_category_value):
    wait = WebDriverWait(context.browser, 10)
    wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@class=\"android.widget.TextView\"]")))
    elements = context.browser.find_elements_by_android_uiautomator(
        "new UiSelector().textContains(\"" + sub_category_value + "\")")
    for element in range(len(elements)):
        assert elements[element].is_displayed(), True


@when(u'user searches for product "{product_desc}"')
def step_search_product(context, product_desc):
    wait = WebDriverWait(context.browser, 50)
    wait.until(EC.visibility_of_element_located((MobileBy.ID, "rs_search_src_text")))
    context.browser.find_element_by_id("rs_search_src_text").clear()
    context.browser.find_element_by_id("rs_search_src_text").send_keys(product_desc)
    context.browser.press_keycode(66)


@then(u'validate no products found message for "{product_desc}"')
def step_validate_no_product_message(context, product_desc):
    wait = WebDriverWait(context.browser, 50)
    wait.until(EC.visibility_of_element_located((MobileBy.ID, "rs_no_result_header")))
    assert context.browser.find_element_by_id("rs_no_result_header").get_attribute(
        "text"), "Your search \"" + product_desc + "\"" + " did not match any products."


@then(u'filter products by filter-type "{filter_type}" and value "{filter_value}"')
def step_validate_no_product_message(context, filter_type, filter_value):
    wait = WebDriverWait(context.browser, 50)

    # Open Filter modal
    wait.until(EC.visibility_of_element_located((MobileBy.ID, "rs_filter_icon_header_btn")))
    x = context.browser.find_element_by_id("rs_filter_icon_header_btn").location['x']
    y = context.browser.find_element_by_id("rs_filter_icon_header_btn").location['y']
    context.browser.find_element_by_id("rs_filter_icon_header_btn").click()

    # Select Filter Type
    wait.until(EC.visibility_of_all_elements_located(
        (MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"" + filter_type + "\")")))
    context.browser.find_element_by_android_uiautomator(
        "new UiSelector().text(\"" + filter_type + "\")").click()

    # Select Filter Value
    wait.until(EC.visibility_of_element_located((MobileBy.ACCESSIBILITY_ID, filter_value)))
    context.browser.find_element_by_accessibility_id(filter_value).click()
    wait.until(EC.visibility_of_element_located((MobileBy.ACCESSIBILITY_ID, filter_value + ". Selected")))

    # Close Filter Type
    context.browser.find_element_by_android_uiautomator(
        "new UiSelector().text(\"" + filter_type + "\")").click()
    wait.until(EC.invisibility_of_element_located((MobileBy.ACCESSIBILITY_ID, filter_value + ". Selected")))

    # Close Filter Modal
    actions = TouchAction(context.browser)
    actions.tap(None, x=x, y=y).perform()
    time.sleep(2)


@then(u'sort products with order "{sort_order}"')
def step_sort_products(context, sort_order):
    wait = WebDriverWait(context.browser, 50)

    # Open Sort Modal
    wait.until(EC.visibility_of_element_located((MobileBy.ID, "rs_sort_icon_header_btn")))
    x = context.browser.find_element_by_id("rs_sort_icon_header_btn").location['x']
    y = context.browser.find_element_by_id("rs_sort_icon_header_btn").location['y']
    context.browser.find_element_by_id("rs_sort_icon_header_btn").click()

    # Select Sorting Order
    context.browser.find_element_by_android_uiautomator(
        "new UiSelector().text(\"" + sort_order + "\")").click()
    wait.until(EC.visibility_of_element_located((MobileBy.ID, "refinements_menu_popup_background")))

    # Close Filter Modal
    actions = TouchAction(context.browser)
    actions.tap(None, x=x, y=y).perform()
    time.sleep(2)


@then(u'verify products have been sorted with order "{sort_order}"')
def step_validate_product_sort_order(context, sort_order):
    rates = []
    wait = WebDriverWait(context.browser, 10)
    wait.until(
        EC.visibility_of_all_elements_located((MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().textContains(\"₹\")")))
    elements = context.browser.find_elements_by_android_uiautomator(
        "new UiSelector().textContains(\"₹\")")

    for i in elements:
        if "You Save" in i.text:
            elements.remove(i)

    for element in range(len(elements)):
        print(elements[element].text)
        product_price = re.sub('[^0-9]', '', elements[element].text)
        rates.append(product_price)

    print(rates)

    if "Ascending" in sort_order:
        sort_flag = step_check_sorting("ascending", rates)
    elif "Descending" in sort_order:
        sort_flag = step_check_sorting("descending", rates)

    assert sort_flag, True


