############------------ IMPORTS ------------############
from selenium import webdriver


############------------ FUNCTION(S) ------------############
def delete_inmails():
    # set url
    url = 'https://www.linkedin.com/in/aa-ag/'

    # creates a webdriver object to open the browser
    driver = webdriver.Firefox()

    # opens url
    driver.get(url)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    delete_inmails()