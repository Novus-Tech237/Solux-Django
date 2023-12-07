from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# Set Edge options
edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True  # Ensure you are using Chromium-based Edge
edge_options.add_argument("--headless")  # Add any additional options if needed

# Specify the path to the EdgeDriver executable using the PATH environment variable or provide the full path
# The 'msedgedriver.exe' should be in a directory that is included in your system's PATH variable
driver = webdriver.Edge(options=edge_options)

# Open Instagram's registration page
driver.get('https://www.instagram.com/accounts/emailsignup/')

# Common credentials for all accounts
password = 'Malik12345'
email = 'novustechnologies7@gmail.com'

# Dictionary of 500 names and usernames
name_dict = {
    'Camila Gonzalez': 'itzzz_camila',
    'Ava Young': 'ava_young'
}

for full_name, username in name_dict.items():
    # Fill in the registration form
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'username'))).send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.NAME, 'emailOrPhone').send_keys(email)
    driver.find_element(By.NAME, 'fullName').send_keys(full_name)

    # Submit the form
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Wait for the account creation process to complete
    WebDriverWait(driver, 10).until(EC.url_contains('https://www.instagram.com/accounts/'))

    # Print the account creation confirmation URL and username
    print(f'Account for {full_name} created successfully. Username: {username}, URL: {driver.current_url}')

    # Introduce a delay before attempting login
    time.sleep(10)  # You can adjust the delay as needed

    # Go back to the registration page for the next account
    driver.get('https://www.instagram.com/accounts/emailsignup/')

# Close the browser
driver.quit()
