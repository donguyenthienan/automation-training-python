# import webdriver
from selenium import webdriver

# create webdriver object
driver = webdriver.Chrome()
driver.maximize_window()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element
element = driver.find_element_by_id("gsc-i-id1")

# get tag_name
print(element.tag_name)

driver.close()
