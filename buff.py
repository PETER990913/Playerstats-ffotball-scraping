from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# Create a ChromeOptions instance
options = webdriver.ChromeOptions()

# Replace this with the actual path to your Chrome user profile directory
# options.add_argument("user-data-dir=C:\\Users\\JS guru\\AppData\\Local\\Google\\Chrome\\User Data")

# Disable the "DevToolsActivePort" check, as it can sometimes cause issues
options.add_argument("--disable-dev-shm-usage")

# Disable the "sandbox" mode if you encounter issues
options.add_argument("--no-sandbox")

# Create a Chrome webdriver instance with the options
driver = webdriver.Chrome(options=options)

driver.maximize_window()
# Open a website
driver.get("https://buff.163.com/market/csgo#tab=selling&page_num=1")

# Find the one page table element
Tbody = driver.find_element(By.CSS_SELECTOR, 'div[class="list_card unhover"]')

table_groups = Tbody.find_elements(By.TAG_NAME, 'li')

for table in table_groups:
    Title = table.find_element(By.TAG_NAME, 'h3').text
    print('Title:::', Title)
    Price = table.find_element(By.TAG_NAME, 'strong').text
    Price = str(Price).replace('\n', '')
    print('Price:::', Price)
while True:
    pass