from selenium import webdriver

from getpass import getpass

usr = input('Enter your username or email id: ')

pwd = getpass('Enter your password : ')

driver = webdriver.Chrome()
driver.get('https://twitter.com/login')

username_box = driver.find_element_by_id('[username_or_email]')

username_box.send_keys(usr)

password_box = driver.find_element_by_id('[password]')

password_box.send_keys(pwd)

login_btn = driver.find_element_by_class_name('authenticity_token')

login_btn.submit()
