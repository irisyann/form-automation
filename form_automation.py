# Automate form-filling with Selenium from csv data
# 26 July 2021
# by Peanuto
 
from selenium import webdriver 
# Selenium automates web browsers by providing an interface that allows you  to write test scripts. In this case I am using Python.
from selenium.webdriver.support.ui import Select
import csv
import time

driver = webdriver.Chrome ()
driver.implicitly_wait(0.5)

URL = "YOUR_URL"
# launch the webpage containing information to be processed
driver.get(URL)

############### LOGIN PAGE (comment this section out if no login page is involved) ###############
USERNAME_FIELD = 'USERNAME_FIELD'
PASSWORD_FIELD = 'PASSWORD_FIELD'
USERNAME = 'YOUR_USERNAME' 
PASSWORD = 'YOUR_PASSWORD' 
SUBMIT_BUTTON_NAME = 'SUBMIT_BUTTON_NAME'

# input e-mail
driver.find_element_by_id('USERNAME_FIELD').send_keys("YOUR_USERNAME")

# input password
driver.find_element_by_id('PASSWORD_FIELD').send_keys("YOUR_PASSWORD")

# click login button
driver.find_element_by_name("SUBMIT_BUTTON_NAME").click()

# define name of csv file to be processed
FILENAME = 'YOUR_FILENAME.csv'
ID_FIELD1 = 'FIELD1'
ID_FIELD2 = 'FIELD2'

# loop through each row in csv fle
with open(FILENAME, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        DATA = row[0] # each row contains the data to be processed

        ### START OF FORM ###

        # REGULAR TEXT FIELD
        driver.find_element_by_id(ID_FIELD1).send_keys(DATA) # input data into form

        # FIRST SUBMIT BUTTON (IN THE CASE OF MULTIPLE SUBMIT BUTTONS IN A FORM/PAGE)
        driver.find_element_by_name("SUBMIT_BUTTON_NAME").click() # click submit

        # DROPDOWN MENU
        DROPDOWN = Select(driver.find_element_by_id(ID_FIELD2))
        DROPDOWN.select_by_index(2) # depends on which option should be selected
 
        # SECOND SUBMIT BUTTON
        driver.find_elements_by_name("commit")[1].click() 

        ### END OF FORM PAGE ###

        # sleep but not necessary,personally used this for debugging
        # time.sleep(5) 

        # GO BACK TO FORM PAGE
        driver.back() 

        # REFRESH PAGE TO CLEAR FORM CONTENT
        driver.refresh() 
