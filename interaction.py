
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options )

driver.get("https://en.wikipedia.org/wiki/Main_Page")
'''
find = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(find.text)
'''

#-------Using different methods in order to complete different functions---------#


#Using a click feature
'''
all_portals = driver.find_element(By.LINK_TEXT , value = "Content portals")
all_portals.click()
'''
#portal = driver.find_element(By.LINK_TEXT , v)

#Using the typing keys

'''time.sleep(10)
search = driver.find_element(By.NAME , value= "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)'''

#Filling out a servey
'''
driver.get("https://secure-retreat-92358.herokuapp.com/")
search = driver.find_element(By.NAME , value = "fName")
search.send_keys("Chris")
test = driver.find_element(By.NAME , value = "lName")
test.send_keys("W")
test2 = driver.find_element(By.NAME , value = "email")
test2.send_keys("test@test.com", Keys.ENTER)
'''

# Cookie clicker website

driver.get("https://orteil.dashnet.org/experiments/cookie/")
clicker = driver.find_element(By.ID , value = "cookie" )


item_selector = driver.find_element(By.CSS_SELECTOR , value = "#store div")

