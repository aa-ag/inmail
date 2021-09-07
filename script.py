############------------ IMPORTS ------------############
from selenium import webdriver
from settings import username, password


############------------ GLOBAL VARIABLE(S) ------------############
username = username
password = password

login_url = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'


############------------ FUNCTION(S) ------------############
def delete_inmails():
    # set url
    url = login_url

    # creates a webdriver object to open the browser
    driver = webdriver.Firefox()

    # opens url
    driver.get(url)

    # input username into username field
    driver.find_element_by_id("username").send_keys(username)

     # input password into password field
    driver.find_element_by_id("password").send_keys(password)

    # click on "Sign in" button
    driver.find_element_by_class_name("btn__primary--large from__button--floating")


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    delete_inmails()


# TO DO: 
# https://www.thepythoncode.com/article/automate-login-to-websites-using-selenium-in-python
# https://qavalidation.com/2018/02/handle-dropdown-selenium-using-python.html/
# https://www.geeksforgeeks.org/selenium-python-tutorial/