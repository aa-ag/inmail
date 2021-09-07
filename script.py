############------------ IMPORTS ------------############
### Python
import time
import random
### Self/Program
import settings as s
### Other
from selenium import webdriver


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
    min, max = 3, 8

    # generate a random floating point number
    random_float = min + ((max - min) * random.random())

    return random_float


def delete_inmails():
    '''
     had to temoporarily disable two-factor
     authentication for this.

     opens Firefox, uses credentials and 
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

    # wait to avoid bot-detection
    seconds = generate_random_float()
    time.sleep(seconds)

    # once logged in, navigate to Messaging
    driver.find_element_by_link_text("Messaging").click()

    # wait to avoid bot-detection
    seconds = generate_random_float()
    time.sleep(seconds)

    # click on burger | three dots button
    ### first, expand dropdown
    driver.find_element_by_class_name("artdeco-button__icon").click()

    # wait to avoid bot-detection
    seconds = generate_random_float()
    time.sleep(seconds)

    ### second, click on delete button
    driver.find_element_by_id("ember312").click()

    


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    delete_inmails()