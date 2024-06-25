import unittest
import datetime
import random
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestDanaApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        capabilities = {
            "platformName": "Android",
            "platformVersion": "12",  # Replace with your Android version
            "deviceName": "adb-bd07c5d4-UdMSsc._adb-tls-connect._tcp.",  # Replace with your device name
            "automationName": "UiAutomator2",
            "appPackage": "com.spotify.music",  # Replace with your app's package name
            "appActivity": "com.spotify.music.MainActivity",  # Randomly selected activity
            "ignoreHiddenApiPolicyError": True,  # Add this line if necessary
            "noReset": True
        }
        
        appium_server_url = 'http://localhost:4723'
        cls.driver = webdriver.Remote(appium_server_url, 
                                      options=UiAutomator2Options().load_capabilities(capabilities))

    def test_play_song_in_playlist(self):
        try:
            # Wait for the "Your Library" button to be visible and click on it
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((AppiumBy.ID, 'com.spotify.music:id/your_library_tab'))
            )
            your_library_button = self.driver.find_element(by=AppiumBy.ID, value='com.spotify.music:id/your_library_tab')
            your_library_button.click()

            # Wait for playlists to load (assuming playlists are displayed after clicking 'Your Library')
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((AppiumBy.ID, 'com.spotify.music:id/playlist_row'))
            )

            # Example: Click on the "Calm" playlist (adjust as per your app's UI structure and playlist name)
            playlist_name = "Calm"
            playlist = self.driver.find_element(by=AppiumBy.XPATH, value=f"//*[contains(@text, '{playlist_name}')]")
            playlist.click()

            action_description = f"Opened '{playlist_name}' playlist in Spotify"
            self.log_action(action_description)

            # Wait for songs in the playlist to load (adjust timeout as per your app's performance)
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((AppiumBy.ID, 'com.spotify.music:id/title'))
            )

            # Get all song elements in the playlist
            song_elements = self.driver.find_elements(by=AppiumBy.ID, value='com.spotify.music:id/title')

            # Shuffle the song elements to play them randomly
            random.shuffle(song_elements)

            # Play each song (adjust the number of songs to play)
            num_songs_to_play = min(5, len(song_elements))  # Play at most 5 songs or fewer if playlist has less
            for i in range(num_songs_to_play):
                song_elements[i].click()
                time.sleep(5)  # Wait for 5 seconds to simulate song playing

                # Log the action of playing the song
                song_name = song_elements[i].text
                action_description = f"Played song '{song_name}' from '{playlist_name}' playlist"
                self.log_action(action_description)

                # Go back to the playlist after playing each song
                self.driver.back()
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.XPATH, f"//*[contains(@text, '{playlist_name}')"))
                )
                playlist = self.driver.find_element(by=AppiumBy.XPATH, value=f"//*[contains(@text, '{playlist_name}')]")
                playlist.click()

            test_result = "Test executed successfully!"
        except Exception as e:
            test_result = f"Test failed: {str(e)}"
        
        
        # Writing test result to a text file with timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('spotify_TestResult.txt', 'a') as f:
            f.write(f"\n{timestamp}\n")
            f.write("--------------------------------------------------------------------------------------------\n")
            f.write(f"{test_result}\n")
            f.write(f"{action_description}\n")  # Log the action description
            f.write("--------------------------------------------------------------------------------------------\n")

    def log_action(self, action_description):
        # Log the action with timestamp to the result file
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('spotify_TestResult.txt', 'a') as f:
            f.write(f"{timestamp} - {action_description}\n")

    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
