from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@then(u'user clicks on Shop by Category')
def step_shop_by_category(context):
    wait = WebDriverWait(context.browser, 10)
    wait.until(EC.visibility_of_element_located((By.ID, 'web_home_shop_by_department_label')))
    context.browser.find_element_by_id("web_home_shop_by_department_label").click()


@then(u'validate elements in list view for Shop By Category')
def validate_elements_shop_by_category(context):
    wait = WebDriverWait(context.browser, 10)
    wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//*[contains(@resource-id,'sbdCategory')]")))
    elements = context.browser.find_elements_by_xpath("//*[contains(@resource-id,'sbdCategory')]")
    for element in range(len(elements)):
        assert elements[element].is_displayed(), True


@then(u'user selects "{option}" category')
def step_select_category(context, option):
    wait = WebDriverWait(context.browser, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@content-desc,\"" + option + "\")]")))
    context.browser.find_element_by_xpath("//*[contains(@content-desc,\"" + option + "\")]").click()


@then(u'user selects "{option}" option in category view')
def step_select_category_option(context, option):
    wait = WebDriverWait(context.browser, 10)
    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//android.view.View[contains(@content-desc,\"" + option + "\")]")))
    context.browser.find_element_by_xpath("//android.view.View[contains(@content-desc,\"" + option + "\")]").click()
