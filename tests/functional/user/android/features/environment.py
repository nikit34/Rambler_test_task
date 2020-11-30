from appium import webdriver
from app.application import Application
from behave.log_capture import capture
import logging


BEHAVE_DEBUG_ON_ERROR = True


def before_tag(context, tag):
    if tag.startswith('onboarding'):
        context.onboarding = True
    else:
        del context.onboarding


def before_scenario(context, scenario):
    if "skip" in scenario.effective_tags:
        scenario.skip('[EXPECTED] Scenario was skipped')
        return

    desired_cap = {
      "platformName": "Android",
      "deviceName": "Android Emulator",
      "app": "C:\\Users\\permi\\source\\repos\\draft\\3\\tests\\functional\\user\\android\\src\\app.apk",
      "appPackage": "ru.rambler.kassa",
      "appWaitActivity": "ru.rambler.popcorn.sdk.presentation.screens.main.MainActivity",
      "noReset": "true"
    }
    time_implicitly_wait = 10

    if hasattr(context, 'onboarding'):
        time_implicitly_wait = 5
        desired_cap['noReset'] = "false"
        desired_cap['appWaitActivity'] = "ru.rambler.popcorn.sdk.presentation.screens.onboarding.OnBoardingActivity"

    context.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_cap)
    context.driver.implicitly_wait(time_implicitly_wait)
    context.app = Application(context.driver)


@capture(level=logging.ERROR)
def after_scenario(context, scenario):
    context.driver.quit()

    if 'Status.failed' == scenario.status:
        print("[FAILED] ", scenario.status)


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