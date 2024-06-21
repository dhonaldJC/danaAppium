import logging
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Desired capabilities
desired_caps = {
    "platformName": "Android",
    "platformVersion": "10",  # Replace with your Android version
    "deviceName": "emulator-5554",  # Replace with your device name
    "app": "/path/to/your/app.apk",  # Replace with the path to your APK file
    "automationName": "UiAutomator2",
    "appPackage": "com.danaapp",  # Replace with your app's package name
    "appActivity": "com.danaapp.MainActivity",  # Replace with your app's main activity
}

# Log desired capabilities
logger.info(f"Desired Capabilities: {desired_caps}")

driver = None

try:
    # Attempt to initialize the driver
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    wait = WebDriverWait(driver, 20)

    # Wait until the main screen is loaded
    wait.until(EC.presence_of_element_located((By.ID, "id_of_element_to_wait_for")))

    # Example: Log in to the DANA app
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "id_of_login_button")))
    login_button.click()

    # Wait for login screen
    wait.until(EC.presence_of_element_located((By.ID, "id_of_login_screen_element")))

    # Enter phone number
    phone_number_field = driver.find_element(By.ID, "id_of_phone_number_field")
    phone_number_field.send_keys("your_phone_number")

    # Click next
    next_button = driver.find_element(By.ID, "id_of_next_button")
    next_button.click()

    # Navigate to the transaction history section
    transaction_button = wait.until(EC.element_to_be_clickable((By.ID, "id_of_transaction_button")))
    transaction_button.click()

    # Wait until the transaction history screen is loaded
    wait.until(EC.presence_of_element_located((By.ID, "id_of_transaction_list_element")))

    # Extract transaction data
    transactions = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")

    for transaction in transactions:
        print(transaction.text)

except Exception as e:
    logger.error(f"An error occurred: {e}")

# except TimeoutException as e:
#     print("Timeout waiting for element:", e)
# except NoSuchElementException as e:
#     print("Element not found:", e)
# except Exception as e:
#     print("An error occurred:", e)
finally:
    # Close the app and driver
    if driver:
        driver.quit()
        logger.info("Driver closed.")
