############------------ IMPORTS ------------############
import time
from selenium import webdriver
import settings as s


############------------ GLOBAL VARIABLE(S) ------------############
username = s.username
password = s.password
login_url = s.linkedin_login_page
click = s.form_button


############------------ FUNCTION(S) ------------############
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
    time.sleep(5)

    # input username into username field
    driver.find_element_by_id("username").send_keys(username)

    # wait to avoid bot-detection
    time.sleep(4)

     # input password into password field
    driver.find_element_by_id("password").send_keys(password)

    # wait to avoid bot-detection
    time.sleep(3)

    # click on "Sign in" button
    driver.find_element_by_class_name(click).click()


def delete_inmails():
    pass


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    log_onto_linkedin()

    time.sleep(9.384)

    delete_inmails()