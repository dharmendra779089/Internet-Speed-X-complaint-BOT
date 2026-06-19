from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PROMISED_DOWN = 1000
PROMISED_UP = 1000
Y_EMAIL = "sumankumarmehta82@gmail.com"
Y_PASSWORD = "7jxsT7i4aGGmiqpU"
Y_LOGIN_URL = "https://app.100daysofpython.dev/services/y/login"


class InternetSpeedYBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        wait = WebDriverWait(self.driver, 20)
        
        # Wait up to 20 seconds for the start button to be clickable
        start_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".start-button a")))
        start_button.click()
        
        # We leave the hard sleep here because the speed test physically takes time to run
        time.sleep(60)
        
        self.down = self.driver.find_element(By.CSS_SELECTOR, value=".download-speed").text
        self.up = self.driver.find_element(By.CSS_SELECTOR, value=".upload-speed").text

    def tweet_at_provider(self):
        self.driver.get(Y_LOGIN_URL)
        wait = WebDriverWait(self.driver, 15)

        # Wait up to 15 seconds for the username input to be present in the DOM
        try:
            username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        except:
            # Fallback in case the mock site uses 'email' as the attribute name
            username_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
            
        username_input.send_keys(Y_EMAIL)
        
        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys(Y_PASSWORD)
        password.send_keys(Keys.ENTER)

        # Wait for the tweet compose box to appear
        tweet_compose = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Post text"]')))
        tweet = f"Hey Internet Provider, why is my speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?!"
        tweet_compose.send_keys(tweet)

        # Wait for the tweet button to be clickable
        tweet_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.x-compose-form button')))
        tweet_button.click()

        time.sleep(2) # Brief pause to allow the post request to complete before quitting
        self.driver.quit()


bot = InternetSpeedYBot()
bot.get_internet_speed()
bot.tweet_at_provider()