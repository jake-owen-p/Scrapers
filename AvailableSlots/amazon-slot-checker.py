from selenium import webdriver
import time
import os
import random
import sys

def login(browser):
    browser.find_element_by_name("lsPostalCode").send_keys(sys.argv[2])
    browser.find_element_by_class_name("a-button-input").click()
    time.sleep(1)
    browser.get('https://primenow.amazon.co.uk/account/address')

    browser.find_element_by_name("email").send_keys(sys.argv[3])
    browser.find_element_by_name("password").send_keys(sys.argv[4])
    browser.find_element_by_id("signInSubmit").click()

def navigate_to_checkout(browser):
    time.sleep(1)
    browser.get('https://primenow.amazon.co.uk/cart?ref_=pn_gw_nav_cart')

def generate_random_interval(type):
    if(type=="Notification"):
        return random.randint(9,15)
    if(type=="Browsing"):
        return random.randint(10,20)

def notify_user_slot_available():
    x=10
    while(x >0):
        time.sleep(generate_random_interval("Notification"))
        os.system("say Amazon has a slot available")
        x-=1
    time.sleep(300)
    return

def notify_user_error():
    x=10
    while(x >0):
        time.sleep(generate_random_interval("Notification"))
        os.system("say An error occurred")
        x-=1
    time.sleep(300)
    return

def check_if_slot_available(browser):
    try:
        browser.find_element_by_link_text('Proceed to checkout').click()
        deliverySlotForm = browser.find_element_by_name("deliverySlotForm")
        deliverySlotText = deliverySlotForm.find_element_by_tag_name('span').text
        if("No delivery windows" not in deliverySlotText):
            slotAvailable = True
            notify_user_slot_available()
    except Exception as e:
        print("Error checking slots")
        print(e)
        print("Starting again...")
        browser.quit()
        find_slots()

def find_slots():
    slotAvailable = False 
    browser = webdriver.Chrome(sys.argv[1])
    browser.get('https://primenow.amazon.co.uk/')

    login(browser)
    navigate_to_checkout(browser)

    while(not slotAvailable):
        time.sleep(generate_random_interval("Browsing"))
        check_if_slot_available(browser)
        time.sleep(generate_random_interval("Browsing"))
        browser.back()

find_slots()