from appium import webdriver
from app.application import Application


def before_senario(context, scenario):
    desired_cap = {
      "platformName": "Android",
      "deviceName": "Android Emulator",
      "app": "C:\\Users\\permi\\source\\repos\\draft\\3\\tests\\functional\\user\\android\\src\\app.apk",
      "appPackage": "ru.rambler.kassa",
      "appWaitActivity": "ru.rambler.popcorn.sdk.presentation.screens.onboarding.OnBoardingActivity"
    }
    context.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_cap)
    context.driver.implicitly_wait(5)
    context.app = Application(context.driver)


def after_scenario(context, scenario):
    context.driver.quit()

