from appium import webdriver
from app.application import Application
from behave.log_capture import capture
import logging


BEHAVE_DEBUG_ON_ERROR = True


def before_tag(context, tag):
    if tag.startswith('onboarding'):
        context.onboarding = True
        print('[EXPECTED] Configuration set switch done on ONBOARDING')
    elif tag.startswith('order_place'):
        context.order_place = True
        print('[EXPECTED] Configuration set switch done on ORDER_PLACE')
    else:
        if hasattr(context, 'onboarding'):
            del context.onboarding
        if hasattr(context, 'order_place'):
            del context.order_place
        print('[EXPECTED] Configuration set switch done on MAIN')


def before_scenario(context, scenario):
    if "skip" in scenario.effective_tags:
        scenario.skip('[EXPECTED] Scenario was skipped')
        return

    desired_cap = {
      "platformName": "Android",
      "deviceName": "emulator-5554",
      "app": "C:\\Users\\permi\\source\\repos\\draft\\3\\tests\\functional\\user\\android\\src\\app.apk",
    }
    time_implicitly_wait = 5

    if hasattr(context, 'onboarding'):
        time_implicitly_wait = 5
        desired_cap['noReset'] = "false"
        desired_cap['appPackage'] = "ru.rambler.kassa"
        desired_cap['appActivity'] = "ru.rambler.popcorn.sdk.presentation.screens.main.MainActivity"
        desired_cap['appWaitActivity'] = "ru.rambler.popcorn.sdk.presentation.screens.onboarding.OnBoardingActivity"
    elif hasattr(context, 'order_place'):
        time_implicitly_wait = 10
        desired_cap['noReset'] = "true"
        desired_cap['appPackage'] = "ru.rambler.kassa"
        desired_cap['appActivity'] = "ru.rambler.popcorn.sdk.presentation.screens.main.MainActivity"
    else:
        desired_cap['noReset'] = "true"
        desired_cap['appPackage'] = "ru.rambler.kassa"
        desired_cap['appActivity'] = "ru.rambler.popcorn.sdk.presentation.screens.main.MainActivity"

    context.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_cap)
    context.driver.implicitly_wait(time_implicitly_wait)
    context.app = Application(context.driver)


@capture(level=logging.ERROR)
def after_scenario(context, scenario):
    context.driver.quit()

    print('scenario status: ', scenario.status)


def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")


def before_all(context):
    setup_debug_on_error(context.config.userdata)
    # context.config.setup_logging(
    #     level=logging.DEBUG,
    #     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    #     datefmt='%a, %d %b %Y %H:%M:%S',
    #     filename='testt.log',
    #     filemode='a'
    # )