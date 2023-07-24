import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Define the username and password of the Instagram account you want to add followers to
username = "your_username"
password = "your_password"

# Open the Chrome browser and navigate to Instagram login page
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")

# Find the username and password fields and enter the credentials
username_field = driver.find_element_by_name("username")
password_field = driver.find_element_by_name("password")
username_field.send_keys(username)
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

# Wait for the page to load and find the follow button
time.sleep(5)
follow_button = driver.find_element_by_xpath("//button[contains(text(), 'Follow')]")

# Click on the follow button 5000 times to add 5000 followers to the account
for i in range(5000):
    follow_button.click()
    time.sleep(2)

# Close the browser window
driver.quit()
