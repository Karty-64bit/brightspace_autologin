###############################################################################
# Name: BoilerKey Automated Login 
# Author: Karteikay Dhuper
# Date: May 19th 2021
# Description: This program takes my two-factor authentication password and 
# automatically logs me in to the Purdue Brightspace web portal. The web
# automation is done by utilizing the Selenium module in Python.
###############################################################################

from selenium import webdriver
# –––––––––––– U.I Initialization (before automation begins) ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

print('')
print(''.center(125,'#')+'\n')
print("> BoilerKey Automated Login Script (B.a.l.s) <".center(125,'–')+'\n')
print("👋 Welcome back, Karty!")

two_factor_number = input("\n📝 Please enter your 6-digit two factor authentication code from Duo Mobile. ")

while len(two_factor_number) != 6:
	print(f"\n  [❗] The number you entered is {len(two_factor_number)} digits long. Please enter a 6-digit number.", end = ' ')
	two_factor_number = input("")

print("\n✅ Two-factor retrieved.")
print("\n🚀 Starting automation...")
print("> Sit tight. <".center(125,'-'))
print('\n'+''.center(125,'#')+'\n')

# ––––––––––––––– Automation Logic ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

# safari web driver initialization and redirection to Purdue Brightspace webpage
driver = webdriver.Safari()
driver.get('https://purdue.brightspace.com/d2l/login?sessionExpired=0&target=%2fd2l%2fhome%2f6824')
campus = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/p[2]/a[1]')
campus.send_keys('\n')
campus.click()

# finding and entering username credentials
loginID = driver.find_element_by_xpath('//*[@id="username"]')
loginID.send_keys('kdhuper')

# finding and entering password credentials
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('1525,'+two_factor_number)

# pressing the login button
password_enter = driver.find_element_by_xpath('//*[@id="password"]')
# login_button.click() <-- click function not working for some reason
password_enter.send_keys('\n')

#failed = driver.find_element_by_xpath('//*[@id="status"]')

