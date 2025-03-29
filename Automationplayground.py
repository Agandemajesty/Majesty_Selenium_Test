import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Variable declaration
wait = 10
url = "https://automationplayground.com/crm/login.html"
email = "majesty@gmail.com"
password = "password"
EmailAddress = "agande@yahoo.com"
FirstName = "Agande"
LastName = "Majesty"
City = "Lekki"

# Browser Initialization
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

# Wait for page to load
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "email-id")))

# Login Details
driver.find_element(By.ID, "email-id").send_keys(email)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.ID, "remember").click()
driver.find_element(By.ID, "submit-id").click()

# Wait until login is successful
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "new-customer")))

# New customer On-boarding
driver.find_element(By.ID, "new-customer").click()
driver.find_element(By.ID, "EmailAddress").send_keys(EmailAddress)
driver.find_element(By.ID, "FirstName").send_keys(FirstName)
driver.find_element(By.ID, "LastName").send_keys(LastName)
driver.find_element(By.ID, "City").send_keys(City)

# Handle Dropdown for State Selection
state_dropdown = Select(driver.find_element(By.ID, "StateOrRegion"))
state_dropdown.select_by_value("CO")

# Select Gender
driver.find_element(By.NAME, "gender").send_keys("male")

# Click the Submit button
driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

# Click the Sign-Out button using its link text
driver.find_element(By.LINK_TEXT, "Sign Out").click()

# Wait before closing
time.sleep(wait)

