from appium import webdriver
from selenium.webdriver.common.by import By

desired_cap = {
    "platformName": "Android",
    "deviceName": "Android Emulator",
    "app": "C:\\Users\\permi\\source\\repos\\draft\\3\\app.apk",
    "appPackage": "ru.rambler.kassa",
    "appWaitActivity": "ru.rambler.popcorn.sdk.presentation.screens.onboarding.OnBoardingActivity",
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_cap)
driver.implicitly_wait(5)

e = driver.find_element(By.ID, 'ru.rambler.kassa:id/text_title')
print(e.text)
