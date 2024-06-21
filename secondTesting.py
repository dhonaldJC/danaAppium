from appium.webdriver.webdriver import WebDriver
from typing import Any, Dict
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'platformVersion': '10',  # Replace with your emulator's Android version
    'deviceName': 'emulator-5554',  # Replace with your emulator's name
    'browserName': 'Chrome',  # Specify the browser name as Chrome
}

server_url = 'http://localhost:4723'
options = UiAutomator2Options().load_capabilities(cap)

try:
    driver: WebDriver = WebDriver(command_executor=server_url, options=options)
    driver.get('https://www.google.com/maps')

    el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
    el.click()

finally:
    if 'driver' in locals() or 'driver' in globals():
        driver.quit()
