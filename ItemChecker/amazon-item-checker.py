from selenium import webdriver
import time
import os
import random
import sys
from selenium.common.exceptions import NoSuchElementException

def initAndLogin(browser):
    print("Logging in...")
    browser.get('https://www.amazon.co.uk/')
    time.sleep(1)
    browser.find_element_by_id("nav-link-accountList").click()
    browser.find_element_by_name("email").send_keys(sys.argv[2])
    browser.find_element_by_id("continue").click()
    time.sleep(1)
    browser.find_element_by_name("password").send_keys(sys.argv[3])
    browser.find_element_by_id("signInSubmit").click()
    print("Logging in successfully")

def check_for_item(browser, itemFound):
    try:
        print("Checking item")
        browser.get(sys.argv[4])
        browser.find_element_by_id("outOftock")
    except NoSuchElementException as e:
        notify_user_item_found()
    except Exception as e:
        print("Error checking slots")
        print(e)
        print("Starting again...")
        browser.quit()
        find_item()

def notify_user_item_found():
    print("ITEM FOUND! PURCHASE IT!")
    x=10
    while(x >0):
        time.sleep(generate_random_interval("Notification"))
        os.system("say Amazon has your item")
        x-=1
    time.sleep(300)
    return

def generate_random_interval(type):
    if(type=="Notification"):
        return random.randint(9,15)
    if(type=="Browsing"):
        return random.randint(10,20)

def find_item():
    print("Looking for item " + sys.argv[4])
    itemFound = False 
    browser = webdriver.Chrome(sys.argv[1])

    initAndLogin(browser)
    while(not itemFound):
        print("Refreshing...")
        time.sleep(generate_random_interval("Browsing"))
        check_for_item(browser, itemFound)

find_item()