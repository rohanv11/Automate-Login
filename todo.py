from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


usernamestr = "your_email_goes_here"
passwordstr = "your_password_goes_here"

browser = webdriver.Chrome()
browser.get(('https://login.live.com/oauth20_authorize.srf?response_type=token&client_id=000000004C18365E&redirect_uri=https%3A%2F%2Ftodo.microsoft.com%2Fauth%2Fcallback&scope=https://graph.microsoft.com/User.Read&state=eyJ0b2tlblR5cGUiOiJncmFwaFRva2VuIiwiZmxvd1R5cGUiOiJtc2EifQ==&aadredir=1'))

username = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='loginfmt']")))
username.send_keys(usernamestr)

enter = browser.find_element_by_xpath("//input[@id='idSIButton9']")
enter.click()

password = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='passwd']")))
password.send_keys(passwordstr)

enter = browser.find_element_by_xpath("//input[@id='idSIButton9']")
enter.click()

yes_to_auto_login = browser.find_element_by_xpath("//input[@id='idSIButton9']")
yes_to_auto_login.click()



while(True):
    pass