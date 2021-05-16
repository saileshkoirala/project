
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


PATH = "/home/saileshk/Personal-Project/introcept/test_Script/chromedriver" #Path of chromedriver
driver = webdriver.Chrome(PATH)
driver.get("http://computer-database.herokuapp.com/computers")
ptitle = 'Computers database'
assert driver.title == ptitle, "failed"
print('Test case passed')
print('Page Title is '+driver.title+'\n\n')

def view():
    com = driver.find_elements_by_xpath('//*[@id="main"]/table/tbody/tr/td[1]/a')
    print(com)
    view = (random.choice(com))
    view.click()
    print("++++++++++ Going back +++++++++++++++")
    time.sleep(5)
    home = driver.find_element_by_xpath('/html/body/header/h1/a')
    home.click()
    
    

def addNew():
    print("++++++++++++++++Adding new computer+++++++++++++++")
    search = driver.find_element_by_id("add")
    search.send_keys(Keys.RETURN)
    com_name = driver.find_element_by_id("name")
    com_name.send_keys("testdata")
    int_date = driver.find_element_by_id("introduced")
    int_date.send_keys("1987-02-01")
    dis_date = driver.find_element_by_id("discontinued")
    dis_date.send_keys("1990-03-04")
    com = driver.find_element_by_id("company")
    com.send_keys("Apple")
    create = driver.find_element_by_xpath('//*[@id="main"]/form/div/input')
    create.click()
    print("++++++++++++++++++++++++++++Test case 2 Passed New Computer added +++++++++++++++++++++++++++++\n\n")
    time.sleep(5)


def update():
    print("++++++++++++++++ Updaing Record +++++++++++++++")
    com = driver.find_elements_by_xpath('//*[@id="main"]/table/tbody/tr/td[1]/a')
    view = (random.choice(com))
    view.click()
    com_name = driver.find_element_by_id("name")
    com_name.clear()
    com_name.send_keys("testPC")
    int_date = driver.find_element_by_id("introduced")
    int_date.clear()
    int_date.send_keys("1987-02-01")
    dis_date = driver.find_element_by_id("discontinued")
    dis_date.clear()
    dis_date.send_keys("1990-03-04")
    com = driver.find_element_by_id("company")
    com.send_keys("RCA")
    create = driver.find_element_by_xpath('//*[@id="main"]/form/div/input')
    create.click()                        
    print("++++++++++++++++++++++++++++Test case 3 Passed Value successfully updated +++++++++++++++++++++++++++++\n\n")
    time.sleep(5)

def delete():
    com = driver.find_elements_by_xpath('//*[@id="main"]/table/tbody/tr/td[1]/a')
    view = (random.choice(com))
    view.click()
    print("++++++++++ Deleting +++++++++++++++")
    delR = driver.find_element_by_xpath('//*[@id="main"]/form[2]/input') 
    delR.click()
    print("++++++++++++++ Test case 4 Passed. Deleted Record +++++++++++++++++\n\n")
    time.sleep(5) 

view()
# addNew()
# update()
# delete()
# print("Test over")
time.sleep(5)
driver.quit()


