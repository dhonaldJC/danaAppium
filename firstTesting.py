import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

class TestAppium(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        capabilities = {
            "platformName": "Android",
            "platformVersion": "10",  # Replace with your Android version
            "deviceName": "emulator-5554",  # Replace with your device name
            "automationName": "UiAutomator2",
            "appPackage": "com.android.settings",  # Replace with your app's package name
            "appActivity": ".Settings",  # Replace with your app's main activity
        }
        appium_server_url = 'http://localhost:4723'
        cls.driver = webdriver.Remote(appium_server_url, 
                                      options=UiAutomator2Options().load_capabilities(capabilities))

    def test_find_battery(self):
        try:
            el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
            self.assertIsNotNone(el, "Battery element not found")
            el.click()
            # Add assertion to verify you are on the Battery screen (example assertion)
            battery_title = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
            self.assertEqual(battery_title.text, "Battery")
        except Exception as e:
            self.fail(f"Test failed with exception: {str(e)}")

    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
