import time

from appium.webdriver.common.touch_action import TouchAction
from behave import fixture, use_fixture
from appium import webdriver


app_configMap = {}
app_configMap['Amazon'] = 'in.amazon.mShop.android.shopping', 'com.amazon.mShop.home.HomeActivity'
app_configMap['Calculator'] = 'com.android.calculator2', 'com.android.calculator2.Calculator'


@fixture
def browser_firefox(context):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'emulator-5554'

    configlist = app_configMap.get("Amazon")

    desired_caps['appPackage'] = configlist[0]
    desired_caps['appActivity'] = configlist[1]
    desired_caps['autoDismissAlerts'] = True
    desired_caps['autoGrantPermissions'] = True

    context.browser = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    time.sleep(5)




    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


def before_all(context):
    use_fixture(browser_firefox, context)

