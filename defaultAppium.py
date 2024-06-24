from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

def main():
    capabilities = {
        "platformName": "Android",
        "platformVersion": "10",  # Replace with your Android version
        "deviceName": "emulator-5554",  # Replace with your device name
        "automationName": "UiAutomator2",
        "appPackage": "com.android.settings",  # Replace with your app's package name
        "appActivity": ".Settings",  # Replace with your app's main activity
    }
    appium_server_url = 'http://localhost:4723'
    
    driver = webdriver.Remote(appium_server_url, 
                              options=UiAutomator2Options().load_capabilities(capabilities))
    
    try:
        el = driver.find_element(by=AppiumBy.XPATH, 
                                 value='//*[@text="Battery"]')
        el.click()
    finally:
        driver.quit()

if __name__ == '__main__':
    main()
