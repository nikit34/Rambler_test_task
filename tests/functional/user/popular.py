from appium import webdriver

desired_cap = {
  "platformName": "Android",
  "deviceName": "Android Emulator",
  "app": "C:\\Users\\permi\\source\\repos\\draft\\3\\app.apk",
  "appPackage": "ru.rambler.kassa",
  # "appWaitActivity": "ru.rambler.popcorn.sdk.presentation.screens.main.MainActivity",
  "automationName": "UiAutomator2"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
