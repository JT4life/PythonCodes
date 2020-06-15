from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://facebook.com")

driver.save_screenshot("C:\\Users\\JT\\Desktop\\screenshotfb.png")
