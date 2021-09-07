############------------ IMPORTS ------------############
import time
from selenium import webdriver
import settings as s
import random 


############------------ GLOBAL VARIABLE(S) ------------############
username = s.username
password = s.password
login_url = s.linkedin_login_page
click = s.form_button


############------------ FUNCTION(S) ------------############
###--- HELPER FUNCTION(S) ---################################
def generate_random_float():
    '''
     generates a random float from 3 to 8
    '''

    # sets specific range
    min = 3
    max = 8

    # generate a random floating point number
    random_float = min + ((max - min) * random.random())

    return random_float


def log_onto_linkedin():
    '''
     had to temoporarily disable two-factor
     authentication for this.

     opents Firefox, uses credentials and 
     logs into linkedin, and takes short breaks
     in between steps
    '''
    # set url
    url = login_url

    # creates a webdriver object to open the browser
    driver = webdriver.Firefox()

    # opens url
    driver.get(url)

    # wait to avoid bot-detection
    seconds = generate_random_float()
    time.sleep(seconds)

    # input username into username field
    driver.find_element_by_id("username").send_keys(username)

    # wait to avoid bot-detection
    seconds = generate_random_float()
    time.sleep(seconds)

     # input password into password field
    driver.find_element_by_id("password").send_keys(password)

    # wait to avoid bot-detection
    seconds = generate_random_float()
    time.sleep(seconds)

    # click on "Sign in" button
    driver.find_element_by_class_name(click).click()


def delete_inmails():
    pass


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    # log_onto_linkedin()

    generate_random_float()

    # time.sleep(3)

    # delete_inmails()