# In this file we are going to learn how to use selenium , 
# to automate filling out forms for us. Such as job applications  , 
# Google forms , etc.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
#Creating our options for our driver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
#Creating and setting up our webdriver

driver = webdriver.Chrome(options= chrome_options)

#Getting amazon link. 
'''
driver.get("https://www.amazon.com/uni-Aluminum-Thunderbolt-Multiport-Chromebook/dp/B087QFM3GF/ref=sr_1_2_sspa?crid=1BO4U8T1TS9KG&dib=eyJ2IjoiMSJ9.PZ5Elpx-mwwDrLcqT_sNYQwpucXw4fgqOm1myD4rdRLmqLZiyUVR-wqX10Xh9qHA6FQ8rT5bBEC63b-P7O8beDYM4ANt8ltmxjBMOFoEui0oYLPkA5IwAKSeOZkeuO3EAb2toZPdNOjbrKcbtcQsABFTUbWlQaljWy1fUsVjIHq_9qeEwcsOE5f9rlxJH84fVxFHAW8LXfVlAbC3Zb-LIJnobnolkjLrOa9KVAbSLAw.kmJJaCughuep81jXtGcnuCUEF3ZK9L1xrQ2-Sn4xFao&dib_tag=se&keywords=usbc%2Bto%2Busb%2Badapter&qid=1746215354&sprefix=%2Caps%2C178&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")
time.sleep(15)

price_dollar = driver.find_element(By.CLASS_NAME , value = "a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME , value = "a-price-decimal")
print(f"The price is ${price_dollar.text}.{price_cents.text}")
'''
#Getting a input link / search bar
'''
driver.get("https://www.python.org/")
time.sleep(15)

search_box = driver.find_element(By.NAME , value="q")
print(search_box.get_attribute("placeholder"))



#Using an XPATH, 'Copy from google , copy as xpath , then paste in here

bug_reporter = driver.find_element(By.XPATH , value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_reporter.text)
driver.quit()
'''

##----------------Challenge-----------------##
#Scrape website data and be able to print a dictionary of the upcoming events
#From the python website

driver.get("https://www.python.org/")

upcoming_events = driver.find_elements(By.CSS_SELECTOR , value=".event-widget time")
event_name = driver.find_elements(By.CSS_SELECTOR , value=".event-widget a" )

my_dict = {}

for n in range(len(upcoming_events)):
    my_dict[n] = {
        "time": upcoming_events[n].text ,
        "name": event_name[n].text
    }
print(my_dict)
driver.quit()