import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of Chrome WebDriver
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Navigate to the URL
driver.get("https://labour.gov.in/")

try:
    # Wait for the "Documents" menu to be clickable
    documents_menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Documents')]")))

    # Click on the "Documents" menu
    documents_menu.click()

    # Find and click on the "Monthly Progress Report" link
    monthly_progress_report_link = driver.find_element(By.XPATH, "//a[contains(text(),'Monthly Progress Report')]")
    monthly_progress_report_link.click()

    # Wait for the page to load
    time.sleep(2)

    # Go back to the home page
    driver.back()

    # Go to the "Media" menu
    media_menu = driver.find_element(By.XPATH, "//a[contains(text(),'Media')]")
    media_menu.click()

    # Find and click on the "Photo Gallery" submenu
    photo_gallery_submenu = driver.find_element(By.XPATH, "//a[contains(text(),'Photo Gallery')]")
    photo_gallery_submenu.click()

    # Wait for the page to load
    time.sleep(2)

    # Create a folder to store downloaded photos
    folder_name = "downloaded_photos"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Find all photo elements
    photo_elements = driver.find_elements(By.XPATH, "//img[@class='attachment-medium size-medium']")
    photo_urls = [element.get_attribute('src') for element in photo_elements]

    # Download and save each photo in the folder
    for i, photo_url in enumerate(photo_urls[:10]):  # Downloading only first 10 photos
        photo_path = os.path.join(folder_name, f"photo_{i+1}.jpg")
        with open(photo_path, 'wb') as f:
            f.write(requests.get(photo_url).content)

    # Close the browser
    driver.quit()

except Exception as e:
    print("An error occurred:", e)
    # Close the browser in case of error
    driver.quit()