import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import datetime

class TestAppium(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        capabilities = {
            "platformName": "Android",
            "platformVersion": "12",  # Replace with your Android version
            "deviceName": "adb-bd07c5d4-UdMSsc._adb-tls-connect._tcp.",  # Replace with your device name
            "automationName": "UiAutomator2",
            "appPackage": "com.miui.securitycenter",  # Replace with your app's package name
            "appActivity": "com.miui.powercenter.PowerMainActivity",  # Replace with your app's main activity
            "ignoreHiddenApiPolicyError": True,  # Add this line
            "noReset": True
        }
        appium_server_url = 'http://localhost:4723'
        cls.driver = webdriver.Remote(appium_server_url, 
                                      options=UiAutomator2Options().load_capabilities(capabilities))

    def test_find_battery(self):
        try:
            el = self.driver.find_element(by=AppiumBy.XPATH, 
                                          value='//*[@text="Battery"]')
            el.click()
            test_result = "Test executed successfully!"
        except Exception as e:
            test_result = f"Test failed: {str(e)}"
        
        # Writing test result to a text file with timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('test_results.txt', 'a') as f:
            f.write(f"\n{timestamp}\n")
            f.write("--------------------------------------------------------------------------------------------\n")
            f.write(f"{test_result}\n")
            f.write("--------------------------------------------------------------------------------------------\n")

    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
