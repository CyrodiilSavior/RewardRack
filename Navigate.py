from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





memecount = 0
s1Buttons = "Earn3.00MorePoints"
s2Buttons = "Earn6.00MorePoints"
s3Buttons = "Earn4.00MorePoints"
s4Buttons = "Earn2.00MorePoints"
claimButtons = "ClaimPoints"
s1 = "DISCOVERUNIVISION"
s2 = "DISCOVERBET"
s3 = "discoversmallbet"
s4 = "DISCOVERMASHABLE"
titleCompare1 = "REWARDRACK|OFFER:MASHABLE"

title = ""
header1 = ""
parentWindowHandle = None
offerWindowHandle = None


def titleCheck():
    global s1Buttons
    global s2Buttons
    global s3Buttons
    global s4Buttons
    global s1
    global s2
    global s3
    global s4
    global titleCompare1
    global title
    global header1
    global parentWindowHandle
    global offerWindowHandle
    global memecount
    if memecount<1:
	    while not parentWindowHandle:
                parentWindowHandle = browser.current_window_handle
            browser.find_element_by_xpath("//button").click()
        
    while not offerWindowHandle:
        for handle in browser.window_handles:
            if handle != parentWindowHandle:
                offerWindowHandle = handle
                break
    browser.switch_to_window(offerWindowHandle)
    title=browser.title
    print "Current Window is " + title

    title = title.replace(" ","")




def univision():
    global s1Buttons
    global s2Buttons
    global s3Buttons
    global s1
    global s2
    global s3
    global titleCompare1
    global title
    global header1
    global parentWindowHandle
    global offerWindowHandle
    global memecount
    waiter = WebDriverWait(browser, 180)
    element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
    print "Step one done waiting"
    browser.find_element_by_link_text("Next Step").click()
    element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
    print "Step two done waiting"
    browser.find_element_by_link_text("Next Step").click()
    element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
    print "Step three done waiting"
    browser.find_element_by_link_text("Next Step").click()
    element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
    print "Step four done waiting"
    browser.find_element_by_link_text("Next Step").click()
    element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
    print "Step five done waiting"
    browser.find_element_by_link_text("Next Step").click()
    element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
    print "Step six done waiting"
    browser.find_element_by_link_text("Next Step").click()
    element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
    print "Step seven done waiting"
    browser.find_element_by_link_text("Next Step").click()
    element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
    print "Step eight done waiting"
    browser.find_element_by_link_text("Next Step").click()
    element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
    print "Step nine done waiting"
    browser.find_element_by_link_text("Next Step").click()
    element = waiter.until(EC.element_to_be_clickable((By.ID,"btn-next-step")))
    print "Step 10 done waiting"
    browser.find_element_by_link_text("Next Step").click()
    element = waiter.until(EC.element_to_be_clickable((By.XPATH,"//a")))
    print "Claim waiting"
    browser.find_element_by_xpath("//a").click()
        

    time.sleep(2)
    memecount += 1
    buttonCheck = browser.find_element_by_xpath("//a").text
    buttonCheck = buttonCheck.replace(" ","")
    #print buttonCheck.lower()
        

    if buttonCheck.lower() == s1Buttons.lower():
        print "next offer button clicked"
        browser.find_element_by_link_text("Earn 3.00 More Points").click()
        header1 = "discoverunivision"
        print "Spanish has continued"

    elif buttonCheck.lower() == s2Buttons.lower():
        print "next offer button clicked"
        browser.find_element_by_link_text("Earn 6.00 More Points").click()
        header1 = "discoverbet"
        offerWindowHandle = None
        print "Black has continued"

    elif buttonCheck.lower() == s3Buttons.lower():
        header1 = "discoversmallbet"
        print "Small bet has continued"
        offerWindowHandle = None
        browser.find_element_by_link_text("Earn 4.00 More Points").click()

    elif buttonCheck.ower() == s4Buttons.lower():
        header1 = discover
        print "mashy has continued"
        OfferWindowHandle = None
        browser.find_element_by_link_text("Earn 2.00 More Points").click()

    else:
        print "Dank has found something new" + buttonCheck.lower()
        browser.find_element_by_xpath("//a").click()






def BET():
    global s1Buttons
    global s2Buttons
    global s3Buttons
    global s1
    global s2
    global s3
    global titleCompare1
    global title
    global header1
    global parentWindowHandle
    global offerWindowHandle
    global memecount
    waiter = WebDriverWait(browser, 180)
    try:
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step one done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step two done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step three done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step four done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step five done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step six done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step seven done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step eight done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step nine done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step ten done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step eleven done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.XPATH,"//button")))
        print "Claim Waiting"
        browser.find_element_by_xpath("//button").click()
    except ValueError:
        print "Black broke"
        
    time.sleep(2)
    memecount += 1
    buttonCheck = browser.find_element_by_xpath("//button").text
    buttonCheck = buttonCheck.replace(" ","")
    print buttonCheck.lower()

    
    if buttonCheck.lower() == s1Buttons.lower():
        header1 = "discoverunivision"
        offerWindowHandle = None
        print "Spanish has continued"
        browser.find_element_by_xpath("//button").click()

    elif buttonCheck.lower() == s2Buttons.lower():
        header1 = "discoverbet"
        print "Black has continued"
        browser.find_element_by_xpath("//button").click()

    elif buttonCheck.lower() == s3Buttons.lower():
        header1 = "discoversmallbet"
	offerWindowHandle = None
        print "Potatoes has continued"
        browser.find_element_by_xpath("//button").click()

    elif buttonCheck.ower() == s4Buttons.lower():
        header1 = discover
        print "mashy has continued"
        OfferWindowHandle = None
        browser.find_element_by_link_text("Earn 2.00 More Points").click()

    else:
        print "Dank has found something new" + buttonCheck.lower()
        browser.find_element_by_xpath("//button").click()




def mashybals():
    global s1Buttons
    global s2Buttons
    global s3Buttons
    global s1
    global s2
    global s3
    global titleCompare1
    global title
    global header1
    global parentWindowHandle
    global offerWindowHandle
    global memecount
    waiter = WebDriverWait(browser, 180)
    try:
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step one done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step two done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step three done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step four done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step five done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step six done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step seven done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step eight done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step nine done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
        print "Step ten done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.XPATH,"//button")))
        print "Claim Waiting"
        browser.find_element_by_xpath("//button").click()
    except ValueError:
        print "something broke potatoes"

    time.sleep(2)
    memecount += 1
    buttonCheck = browser.find_element_by_xpath("//button").text
    buttonCheck = buttonCheck.replace(" ","")
    print buttonCheck.lower()

    
    if buttonCheck.lower() == s1Buttons.lower():
        header1 = "discoverunivision"
        offerWindowHandle = None
        print "Spanish has continued"
        browser.find_element_by_xpath("//button").click()
    elif buttonCheck.lower() == s2Buttons.lower():
        header1 = "discoverbet"
        offerWindowHandle = None
        print "Black has continued"
        browser.find_element_by_xpath("//button").click()
    elif buttonCheck.lower() == s3Buttons.lower():
        header1 = "discoversmallbet"
        print "Small bet has continued"
        browser.find_element_by_xpath("//button").click()

    elif buttonCheck.ower() == s4Buttons.lower():
        header1 = discover
        print "mashy has continued"
        OfferWindowHandle = None
        browser.find_element_by_link_text("Earn 2.00 More Points").click()
        
    else:
        print "Dank has found something new" + buttonCheck.lower()
        browser.find_element_by_xpath("//button").click()    
    




def Mashables():
    global s1Buttons
    global s2Buttons
    global s3Buttons
    global s1
    global s2
    global s3
    global titleCompare1
    global title
    global header1
    global parentWindowHandle
    global offerWindowHandle
    global memecount
    global claimButtons

    waiter = WebDriverWait(browser, 180)
    
    element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
    print "Step one done waiting"
    browser.find_element_by_xpath("//button").click()
    element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
    print "Step two done waiting"
    browser.find_element_by_xpath("//button").click()
    element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
    print "Step three done waiting"
    browser.find_element_by_xpath("//button").click()
    element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
    print "Step four done waiting"
    browser.find_element_by_xpath("//button").click()
    element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
    print "Step five done waiting"
    browser.find_element_by_xpath("//button").click()
    element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
    print "Step six done waiting"
    browser.find_element_by_xpath("//button").click()
    element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
    print "Step seven done waiting"
    browser.find_element_by_xpath("//button").click()
    element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
    print "Step eight done waiting"
    browser.find_element_by_xpath("//button").click()
    element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
    print "Step nine done waiting"
    browser.find_element_by_xpath("//button").click()
    element = waiter.until(EC.element_to_be_clickable((By.ID,"next-step-button")))
    print "Step ten done waiting"
    browser.find_element_by_xpath("//button").click()
    element = waiter.until(EC.element_to_be_clickable((By.XPATH,"//button")))
    buttonCheck = browser.find_element_by_xpath("//button").text
    buttonCheck = buttonCheck.replace(" ","")

    if buttonCheck.lower() == claimButtons.lower():
        browser.find_element_by_xpath("//button").click()
    else:
        print "Step eleven done waiting"
        browser.find_element_by_xpath("//button").click()
        element = waiter.until(EC.element_to_be_clickable((By.XPATH,"//button")))
        print "Claim Waiting"
        browser.find_element_by_xpath("//button").click()    
        
    time.sleep(2)
    memecount += 1
    buttonCheck = browser.find_element_by_xpath("//button").text
    buttonCheck = buttonCheck.replace(" ","")
    print buttonCheck.lower()
    if buttonCheck.lower() == s1Buttons.lower():
        header1 = "discoverunivision"
        offerWindowHandle = None
        print "Spanish has continued"
        browser.find_element_by_xpath("//button").click()
    elif buttonCheck.lower() == s2Buttons.lower():
        header1 = "discoverbet"
        print "Black has continued"
        OfferWindowHandle = None
        browser.find_element_by_xpath("//button").click()
    elif buttonCheck.lower() == s3Buttons.lower():
        header1 = "discoversmallbet"
	offerWindowHandle = None
        print "Potatoes has continued"
        browser.find_element_by_xpath("//button").click()
    elif buttonCheck.ower() == s4Buttons.lower():
        header1 = discover
        print "mashy has continued"
        browser.find_element_by_link_text("Earn 2.00 More Points").click()
    else:
        print "Dank has found something new" + buttonCheck.lower()
        browser.find_element_by_xpath("//button").click()








file = open('Credentials.txt')
info = file.readlines()

usernameWords = info[0].replace("\n","")
passwordWords = info[1]

print usernameWords
print passwordWords

browser = webdriver.Firefox()

browser.delete_all_cookies()
browser.get('http://www.rewardrack.com')
time.sleep(3)
browser.find_element_by_link_text("Sign In").click()

username = browser.find_element_by_id("loginform-username")
username.send_keys(str(usernameWords))

password = browser.find_element_by_id("loginform-password")
password.send_keys(str(passwordWords))

browser.find_element_by_tag_name("button").click()

count = 0
while count < 2:
    time.sleep(1)
    count += 1

browser.get('http://rewardrack.com/offer-wall')

header = browser.find_element_by_xpath("//h5")
print header.text

count = 3
while count > 0:
    time.sleep(1)
    #print str(count) + " Seconds till dank"
    count = count-1

header1 = header.text
header1 = header1.replace(" ","")




while memecount < 60:
    print "current itteration count is: " + str(memecount)
    if  header1.lower() == s1.lower():
        #print "DANK ACHIEVED"

        titleCheck()

        
        if title.lower() == titleCompare1.lower():
            mashybals()
            
        else:
            univision()
            
        

            

    elif header1.lower() == s2.lower():
        #print "Dank BLACK ACHIEVED"
        
	titleCheck()

	BET()

        

    elif header1.lower() == s3.lower():
        # print "DANK SMALL BLACK ACHIEVED"
        titleCheck()

        BET()

    elif header1.lower() == s4.lower():
        #print "Dank potatoes achieved"
        titleCheck()

        Mashables()

    else:
        print "dnak memes are broken"


browser.quit()

curTime = datetime.datetime.now()
curTime_String = str(curTime.strftime("%m/%d/%Y-%H:%M"))
print(curTime_String)


f = open("time.txt", "w")
f.write(curTime_String)
f.close()





