############------------ IMPORTS ------------############
from selenium import webdriver
from settings import username, password


############------------ GLOBAL VARIABLE(S) ------------############
user = username
password = password


############------------ FUNCTION(S) ------------############
def delete_inmails():
    # set url
    url = 'https://www.linkedin.com/feed/?trk=homepage-basic_signin-form_submit'

    # creates a webdriver object to open the browser
    driver = webdriver.Firefox()

    # opens url
    driver.get(url)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    delete_inmails()


# TO DO: 
# https://www.thepythoncode.com/article/automate-login-to-websites-using-selenium-in-python
# https://qavalidation.com/2018/02/handle-dropdown-selenium-using-python.html/
# https://www.geeksforgeeks.org/selenium-python-tutorial/