from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create a new instance of Chrome WebDriver
driver = webdriver.Chrome()

# Open the CoWIN website
driver.get("https://www.cowin.gov.in/")

# Store the current window handle
main_window_handle = driver.current_window_handle

# Find and click on the "FAQ" anchor tag to open a new window
faq_link = driver.find_element(By.XPATH, "//a[contains(text(),'FAQ')]")
faq_link.click()

# Find and click on the "Partners" anchor tag to open another new window
partners_link = driver.find_element(By.XPATH, "//a[contains(text(),'Partners')]")
partners_link.click()

# Wait for the new windows to open
time.sleep(2)

# Get handles of all windows opened by the driver
all_window_handles = driver.window_handles

# Display the window handles
print("Window handles of opened windows:")
for handle in all_window_handles:
    print(handle)

# Close the new windows and switch back to the main window
for handle in all_window_handles:
    if handle != main_window_handle:
        driver.switch_to.window(handle)
        driver.close()

# Switch back to the main window
driver.switch_to.window(main_window_handle)

# Close the browser
driver.quit()