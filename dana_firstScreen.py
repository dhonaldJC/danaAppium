import logging
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    # Desired capabilities
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "10",
        "deviceName": "emulator-5554",
        "app": "/Users/johannessihotang/project/danaAppium/dana.apk",
        "automationName": "UiAutomator2",
        "appPackage": "com.danaapp",
        "appActivity": "com.danaapp.MainActivity",
    }

    # Log desired capabilities
    logger.info(f"Desired Capabilities: {desired_caps}")

    # Initialize the driver
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    logger.info("Appium driver initialized successfully.")

    # Example: Wait for an element to be visible and interact with it
    wait = WebDriverWait(driver, 20)
    element = wait.until(EC.visibility_of_element_located((By.ID, "com.danaapp:id/element_id")))
    element.click()
    logger.info("Element clicked successfully.")

    # Additional test steps...

except Exception as e:
    logger.error(f"An error occurred: {e}")
    # Optionally, you can log the full traceback for debugging purposes
    logger.exception("Full traceback:")

finally:
    # Close the app and driver
    try:
        if 'driver' in locals() or 'driver' in globals():
            driver.quit()
            logger.info("Driver closed.")
    except NameError as ne:
        logger.error(f"NameError occurred: {ne}")
