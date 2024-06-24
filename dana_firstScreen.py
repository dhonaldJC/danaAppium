import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

class TestDanaApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        capabilities = {
            "platformName": "Android",
            "platformVersion": "12",  # Replace with your Android version
            "deviceName": "adb-bd07c5d4-UdMSsc._adb-tls-connect._tcp.",  # Replace with your device name
            "automationName": "UiAutomator2",
            "appPackage": "id.dana",  # Replace with Dana app's package name
            "appActivity": "id.dana.home.HomeTabActivity",  # Replace with Dana app's main activity
        }
        appium_server_url = 'http://localhost:4723'
        cls.driver = webdriver.Remote(appium_server_url, 
                                      options=UiAutomator2Options().load_capabilities(capabilities))

    def test_home_activity(self):
        # Adjust the locator to find a unique element on the home screen of the Dana app
        el = self.driver.find_element(by=AppiumBy.XPATH, 
                                      value='//*[@content-desc="home_activity"]')  # Replace with an actual locator for a unique home screen element
        self.assertIsNotNone(el, "Home activity element not found")
    
    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
