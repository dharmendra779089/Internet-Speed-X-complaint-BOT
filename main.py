# Import the main webdriver module from Selenium to control the browser
from selenium import webdriver
# Import 'By' to specify how we want to locate elements (e.g., by CSS selector, ID, Name)
from selenium.webdriver.common.by import By
# Import 'Keys' to simulate keyboard key presses (like pressing ENTER or TAB)
from selenium.webdriver.common.keys import Keys
# Import 'WebDriverWait' to tell the browser to wait for specific conditions before proceeding
from selenium.webdriver.support.ui import WebDriverWait
# Import 'expected_conditions' (aliased as EC) to define what conditions to wait for (e.g., element is clickable)
from selenium.webdriver.support import expected_conditions as EC
# Import the standard 'time' module to use hard sleep pauses when absolutely necessary
import time

# Define the internet speed you are paying for (Download in Mbps)
PROMISED_DOWN = 1000
# Define the internet speed you are paying for (Upload in Mbps)
PROMISED_UP = 1000
# Your email address used to log into the mock 'Y' (Twitter clone) application
Y_EMAIL = "sumankumarmehta82@gmail.com"
# Your password for the mock 'Y' application (Remember: keep this secret in real life!)
Y_PASSWORD = "YOUR_PASSWORD_HERE" 
# The exact URL where the login form for the 'Y' application is located
Y_LOGIN_URL = "https://app.100daysofpython.dev/services/y/login"


# Define a class to encapsulate all the bot's behaviors and data
class InternetSpeedYBot:
    # The initialization method runs when you create a new instance of the bot
    def __init__(self):
        # Initialize a new Chrome browser window
        self.driver = webdriver.Chrome()
        # Create a variable to store the download speed result, initially set to 0
        self.down = 0
        # Create a variable to store the upload speed result, initially set to 0
        self.up = 0

    # Define a method to run the speed test and scrape the results
    def get_internet_speed(self):
        # Tell the browser to navigate to the Speedtest website
        self.driver.get("https://www.speedtest.net/")
        # Create a 'wait' object that will wait up to 20 seconds for conditions to be met
        wait = WebDriverWait(self.driver, 20)
        
        # Wait until the big "GO" (start) button is present and clickable on the page
        start_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".start-button a")))
        # Click the "GO" button to start the speed test
        start_button.click()
        
        # Force the script to pause for exactly 60 seconds because the test takes time to complete physically
        time.sleep(60)
        
        # Find the element containing the final download speed and extract its text into the self.down variable
        self.down = self.driver.find_element(By.CSS_SELECTOR, value=".download-speed").text
        # Find the element containing the final upload speed and extract its text into the self.up variable
        self.up = self.driver.find_element(By.CSS_SELECTOR, value=".upload-speed").text

    # Define a method to log into the mock 'Y' app and post the tweet
    def tweet_at_provider(self):
        # Tell the browser to navigate to the 'Y' login page
        self.driver.get(Y_LOGIN_URL)
        # Create a 'wait' object that will wait up to 15 seconds for conditions to be met
        wait = WebDriverWait(self.driver, 15)

        # Start a try-except block to handle potential variations in the webpage's HTML
        try:
            # Wait up to 15 seconds for an input field named "username" to appear in the webpage's DOM
            username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        except:
            # If "username" isn't found, try looking for an input field named "email" instead
            username_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
            
        # Type the email address into the located username/email field
        username_input.send_keys(Y_EMAIL)
        
        # Find the password input field by its 'name' attribute
        password = self.driver.find_element(By.NAME, value="password")
        # Type the password into the password field
        password.send_keys(Y_PASSWORD)
        # Simulate pressing the "ENTER" key while focused on the password field to submit the login form
        password.send_keys(Keys.ENTER)

        # Wait until the text box where you compose a tweet is loaded and ready to be clicked
        tweet_compose = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Post text"]')))
        # Format the complaint message using f-strings to inject the measured speeds and promised speeds
        tweet = f"Hey Internet Provider, why is my speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?!"
        # Type the formatted message into the tweet composition box
        tweet_compose.send_keys(tweet)

        # Wait until the "Post" (or "Tweet") button is clickable
        tweet_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.x-compose-form button')))
        # Click the button to publish the tweet
        tweet_button.click()

        # Pause for 2 seconds to ensure the network request to post the tweet has time to complete
        time.sleep(2) 
        # Close the browser window and end the WebDriver session cleanly
        self.driver.quit()


# Create a new instance of our bot class
bot = InternetSpeedYBot()
# Tell the bot to execute the speed test method
bot.get_internet_speed()
# Tell the bot to log in and tweet the results
bot.tweet_at_provider()
