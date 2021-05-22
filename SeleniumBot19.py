import os
from selenium import webdriver

op = webdriver.ChromeOptions()
op.binary_location = '/app/.apt/usr/bin/google-chrome'#os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no--sandbox")
op.add_argument("--disable-dev-sh-usage")

driver = webdriver.Chrome(executable_path='/app/.chromedriver/bin/chromedriver', chrome_options=op)
#"""os.environ.get("CHROMEDRIVER_PATH")"""
driver.get("https://selfregistration.cowin.gov.in/")
print(driver.page_source)
