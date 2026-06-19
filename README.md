# Internet Speed "X" Complaint Bot 🚀

An automated Python script built with Selenium WebDriver that tests your internet speed and automatically "tweets" your ISP on a mock social media platform if you aren't getting the speeds you pay for. 

This project was built as part of the **100 Days of Code: The Complete Python Pro Bootcamp**.

## 📖 Description

Have you ever been frustrated by slow internet speeds? This bot takes matters into its own hands. Using object-oriented programming (OOP) and browser automation, the bot performs the following tasks:
1. Navigates to [Speedtest.net](https://www.speedtest.net/) to run a full download and upload speed test.
2. Extracts the final speed results.
3. Navigates to a mock "Y" (Twitter clone) web application.
4. Logs in using provided credentials.
5. Automatically formats and publishes a post comparing the actual speeds to your promised speeds.

## ✨ Features
* **Fully Automated UI Navigation:** Uses Selenium WebDriver to click buttons, type text, and interact with the DOM.
* **Explicit Waits:** Implements `WebDriverWait` for robust and reliable element detection, preventing crashes caused by slow page loads or network latency.
* **Fallback Logic:** Includes `try/except` blocks to handle minor variations in the website's HTML (e.g., searching for both `username` and `email` input fields).

## 🛠️ Prerequisites

To run this script, you will need:
* **Python 3.x** installed on your machine.
* **Google Chrome** browser installed.
* **Selenium** Python package.

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/internet-speed-bot.git](https://github.com/YOUR_USERNAME/internet-speed-bot.git)
   cd internet-speed-bot
