# selenium_script.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains

# Set the path to your ChromeDriver executable
driver_path = './chromedriver'

# Use the default installation path for Chrome Developer version on macOS
chrome_path = '/Applications/Google Chrome Dev.app/Contents/MacOS/Google Chrome'

# Create a ChromeService object with the path to the Chrome executable
chrome_service = ChromeService(executable_path=chrome_path)

# Specify the ChromeDriver executable path
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--webdriver={driver_path}')

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

# Open the webpage
driver.get("http://pd-net-prod-main-1154509397.us-east-1.elb.amazonaws.com/")

# Take a screenshot of the initial page
driver.save_screenshot("initial_page.png")

# Find and click on navigation links
navigation_links = driver.find_elements_by_xpath("//div[@class='navbar-nav']//a[@class='nav-link']")
for link in navigation_links:
    ActionChains(driver).click(link).perform()
    driver.save_screenshot(f"clicked_{link.text.replace(' ', '_').lower()}.png")

# Find the right arrow button and click on it
right_arrow_button = driver.find_element_by_id("rightArrowButton")
ActionChains(driver).click(right_arrow_button).perform()
driver.save_screenshot("clicked_right_arrow.png")

# Wait for the popup window to be visible
popup_window = driver.find_element_by_id("popupWindow")
driver.implicitly_wait(5)  # Adjust the wait time as needed

# Find and click buttons in the popup window
add_documents_button = driver.find_element_by_id("addDocumentsButton")
ActionChains(driver).click(add_documents_button).perform()
driver.save_screenshot("clicked_add_documents_button.png")

submit_button = driver.find_element_by_id("submitButton")
ActionChains(driver).click(submit_button).perform()
driver.save_screenshot("clicked_submit_button.png")

# Close the browser window
driver.quit()
