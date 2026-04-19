import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
import chromedriver_binary

# Manual .env loader to avoid dependency on python-dotenv
def load_env_file(dotenv_path=".env"):
    if os.path.exists(dotenv_path):
        with open(dotenv_path) as f:
            for line in f:
                if line.strip() and not line.startswith("#"):
                    key, value = line.strip().split("=", 1)
                    os.environ[key] = value

load_env_file()

# Use environment variables for personal data
gender = os.getenv('GENDER', 'X')
firstnameStr = os.getenv('FIRSTNAME', 'YOUR_FIRST_NAME')
surnameStr = os.getenv('SURNAME', 'YOUR_SURNAME')
streetName = os.getenv('STREET', 'YOUR_STREET')
plz = os.getenv('PLZ', 'YOUR_PLZ')
status = os.getenv('STATUS', 'S-RWTH')
mtrNr = os.getenv('MATRIKEL_NR', 'YOUR_MATRIKEL_NR')
email = os.getenv('EMAIL', 'YOUR_EMAIL')
phone = os.getenv('PHONE', 'YOUR_PHONE')

firefoxOptions = Options()
firefoxOptions.headless = True
browser = webdriver.Firefox(options=firefoxOptions, executable_path="./geckodriver")
#if you want to use chrome instead:
#browser = webdriver.Chrome()
browser.get(('https://buchung.hsz.rwth-aachen.de/angebote/aktueller_zeitraum/_Lernraumbuchung.html'))

original_window = browser.current_window_handle
#-----------------------------------------------------------------------------------------

# hour 13:45 this code section should be run
assert len(browser.window_handles) == 1

bookAtOne = browser.find_element(By.NAME,'BS_Kursid_186305')
bookAtOne.click()

# bookAtNine = browser.find_element(By.NAME,'BS_Kursid_186306')
# bookAtNine.click()

# test for medical library
'''
bookAtOne = browser.find_element(By.NAME,'BS_Kursid_186309')
bookAtOne.click()
'''
wait = WebDriverWait(browser, 10)
wait.until(EC.number_of_windows_to_be(2))

for window_handle in browser.window_handles:
    if window_handle != original_window:
        browser.switch_to.window(window_handle)
        break


# change the date to the day before
bookAtOneSecond = browser.find_element(By.NAME,'BS_Termin_2022-06-28')
bookAtOneSecond.click()

#-----------------------------------------------------------------------------------------
# to register without username and password:
#'''

# filloutForm 
# this choice is from radio choices
genderRadio = browser.find_element(By.CSS_SELECTOR,"input[value='X']")
genderRadio.click()

firstnameStrField = browser.find_element(By.ID,'BS_F1100')
firstnameStrField.send_keys(firstnameStr)

surnameStrField = browser.find_element(By.ID,'BS_F1200')
surnameStrField.send_keys(surnameStr)

streetNameStr = browser.find_element(By.ID,'BS_F1300')
streetNameStr.send_keys(streetName)

plzField = browser.find_element(By.ID,'BS_F1400')
plzField.send_keys(plz)

#in choice az dropdown e
statusField = Select(browser.find_element(By.ID,'BS_F1600'))
statusField.select_by_value('S-RWTH')

mtrNrField = browser.find_element(By.ID,'BS_F1700')
mtrNrField.send_keys(mtrNr)

emailField = browser.find_element(By.ID,'BS_F2000')
emailField.send_keys(email)

phoneField = browser.find_element(By.ID,'BS_F2100')
phoneField.send_keys(phone)

checkBox = browser.find_element(By.NAME, 'tnbed')
checkBox.click()

time. sleep(10)

submit = browser.find_element(By.ID, 'bs_submit')
submit.click()
#'''
#-----------------------------------------------------------------------------------------
#to register with user and password:
#to be completed
#do not forget to enter the captcha yourself and to submit your registration


#format examples
#username = browser.find_element(By.ID,'Email')
#username.send_keys(usernameStr)
#nextButton = browser.find_element(By.ID,'next')
#nextButton.click()
#WebElement rbutton = browser.find_element(By.cssSelector("input[value=' Yellow']"))
#rbutton.click()
