from selenium import webdriver
from selenium.common import  exceptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os

import time
import json
import pprint
import csv


##These are the css class to choose the information
class_name = ["_4gus", "_1-sk", "_4guw", "_4gut", "_5rgt _5nk5 _5msi", "_il"]

post=[]

articleContainerClass ="//article[@class='_55wo _5rgr _5gh8 async_like']"

#postLinkXPath ="//div/div[1]/a"
#commentXPath = "//footer/div/div[1]/a/div/div[2]/span"
#reactionXPath ="footer/div/div[1]/a/div/div[1]/div"
fbLink = "https://mobile.facebook.com/"
groupLinks = [
    "https://mobile.facebook.com/groups/3323854697841336/?ref=group_browse",
    "https://mobile.facebook.com/groups/2396795340453227/?ref=group_browse",
    "https://mobile.facebook.com/groups/2232354350372325/?ref=group_browse",
    "https://mobile.facebook.com/groups/1856072608051143/?ref=group_browse",
    "https://mobile.facebook.com/groups/1712424082372481/?ref=group_browse",
    "https://mobile.facebook.com/groups/1606567199558157/?ref=group_browse",
    "https://mobile.facebook.com/groups/1549030312003177/?ref=group_browse",
    "https://mobile.facebook.com/groups/1050735792104175/?ref=group_browse",
    "https://mobile.facebook.com/groups/557339772259465/?ref=group_browse",
    "https://mobile.facebook.com/groups/494938151630057/?ref=group_browse",
    "https://mobile.facebook.com/groups/485595848653433/?ref=group_browse",
    "https://mobile.facebook.com/groups/434661027871196/?ref=group_browse",
    "https://mobile.facebook.com/groups/427336388401184/?ref=group_browse",
    "https://mobile.facebook.com/groups/352120431828349/?ref=group_browse",
    "https://mobile.facebook.com/groups/296525075547264/?ref=group_browse",
    "https://mobile.facebook.com/groups/283780253092282/?ref=group_browse",
    "https://mobile.facebook.com/groups/261658928421492/?ref=group_browse",
    "https://mobile.facebook.com/groups/193427604794787/?ref=group_browse",
    "https://mobile.facebook.com/groups/174021326556602/?ref=group_browse",
    "https://mobile.facebook.com/groups/157070304903101/?ref=group_browse",
    "https://mobile.facebook.com/groups/114975699094438/?ref=group_browse",
    "https://mobile.facebook.com/groups/3073972669330453/?ref=group_browse",
    "https://mobile.facebook.com/groups/2932215260333602/?ref=group_browse",
    "https://mobile.facebook.com/groups/2777314399147797/?ref=group_browse",
    "https://mobile.facebook.com/groups/2267421523507404/?ref=group_browse",
    "https://mobile.facebook.com/groups/2025771334359815/?ref=group_browse",
    "https://mobile.facebook.com/groups/1994886254131045/?ref=group_browse",
    "https://mobile.facebook.com/groups/630353667861611/?ref=group_browse",
    "https://mobile.facebook.com/groups/575029336040752/?ref=group_browse",
    "https://mobile.facebook.com/groups/480658072822702/?ref=group_browse",
    "https://mobile.facebook.com/groups/377436819112288/?ref=group_browse",
    "https://mobile.facebook.com/groups/304222654430887/?ref=group_browse",
    "https://mobile.facebook.com/groups/178202949050334/?ref=group_browse",
    "https://mobile.facebook.com/groups/123383601176136/?ref=group_browse",
    "https://mobile.facebook.com/groups/4458091350904337/?ref=group_browse",
    "https://mobile.facebook.com/groups/1659094737714974/?ref=group_browse"
    ]


sec= int(input("input the processing time: "))
scroll=int(input("input the number of time you want to scroll: "))

words=[]
#listnum = int(input("How many word in the list: "))
def WordList(mot,o):
    n = 1
    while(n>0):
        new = str(input("Insert the keyword #" + str(n) + ": "))
        if new == '0':
            break
        else:
            mot.append(new)
            n+=1
        
#Set up the Chrome options

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)


#specify the path to chromedriver.exe (download and save on your computer) and launch chrome driver
driver = webdriver.Chrome('C:/Users/KING-K-S/pythonWEPO/pythonWEPO/chromedriver.exe',options=chrome_options)
wait = WebDriverWait(driver, 2)




1
#This function loop through the facebook links and open each of them
def OpenLink(li, num):
        print("Now processing Page: "+"\n"+ li)
        driver.get(li)
        time.sleep(3)
        print("\n")
        ##isOnFacebook =" is on Facebook"
        print(">>>Please wait!<<<")


#This function is for login into Facebook

def FbLogin(num):

    try:
        youMust = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/span").text
    except:
        print(exceptions.NoSuchElementException("No message"))
        youMust = "Not logged in"
        

        Clikclogin = button = WebDriverWait(driver, num).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[role='button']"))).click()
        driver.implicitly_wait(num)
    #click the login button
    
    #target username
    username = WebDriverWait(driver, num).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
    password = WebDriverWait(driver, num).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

    #enter username and password (don't worry I made this facebook account just for doing the scrawling and and collecting data)
    username.clear()
    username.send_keys("info.sensmart@gmail.com")
    password.clear()
    password.send_keys("yeswecan")

    driver.implicitly_wait(num)
    #target the login button and click it
    button = WebDriverWait(driver, num).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='button']"))).click()

postContentClass =[]

print("Now collecting the data", end="")
time.sleep(2)
for e in range(3):
    print('.', end="")
    time.sleep(2)
print('\n')



#This is a function to collect data
def Collect(r):
    action_chain = webdriver.ActionChains(driver)
    refresh = driver.refresh()
    print("\n")
    time.sleep(3)

    # A Loop to scroll at the bottom of the page
    for a in range(r*5):
        action_chain.key_down(Keys.END).perform()
        print("scroll " + str(a))
        time.sleep(1)
    print("\n")
    # This is the variable for list of articles we are going to retrieve. 
    listOfArticles = driver.find_elements(By.XPATH, articleContainerClass)    
    #This is a for loop to collect data from every single articles.
    for i in listOfArticles:
        
        #Here we will retrieve the name of the seller, the post content and the post link
        postObject = {}
    #print(i)
        l = i.find_elements(By.CLASS_NAME, "story_body_container")
        
        # Check if it is a shared post or it was posted directly on the group.
        if(len(l) ==2):

            #If it is a shared post
            sellerName = l[1].find_element(By.XPATH,".//strong").text
            postDetail = l[1].find_element(By.XPATH,".//div[@class='_5rgt _5nk5 _5msi']").text
            postLink = fbLink + l[1].find_element(By.XPATH,".//a[@class='_5msj']").get_attribute("href")

        elif(len(l)==1):
            # If it was not shared

            sellerName = l[0].find_element(By.XPATH,".//strong").text
            postDetail = l[0].find_element(By.XPATH,".//div[@class='_5rgt _5nk5 _5msi']").text
            postLink = fbLink + l[0].find_element(By.XPATH,".//a[@class='_5msj']").get_attribute("href")
        
        #Let's shorten the post link 
        numberOfSlash = 0
        temp = []
        for t in postLink:

            if numberOfSlash ==7:
                break
            if t =="/":
                numberOfSlash += 1
            temp.append(t)
        postLink = "".join(temp)
        time.sleep(1)

        # We will save the retrieved data into the post object and save it in our list.

        # Check if the post is not empty
        if(len(postDetail)>0):    
            postObject['sellerName'] = sellerName
            postObject['postDetail'] = postDetail
            postObject['postLink'] = postLink

            # print the collected Data to the console
            print("Seller Name: " + sellerName)
            print("\n")
            print("POST CONTENT\n==== ======" + postDetail + "\n")
            print("Post Link: " + postLink + "\n" )
            time.sleep(1)

        # If the post is empty, we will return an empty object
        else:
            postObject = {}

        # We will check if the post we are trying to save already exist in our post array. If the post already exists we will not save it in the array.
        for i in post:

            #Check if the post already exist in the list

            if postObject['postLink'] == i['postLink']:
                print("This post already exist in the data base.")
            
            # check if the post is empty
            elif postObject == {} :
                print("This post is empty")

            # Add the post in the array if it is not empty   
            else:
                post.append(postObject)
        print("----------------------")
        print("\n")
        time.sleep(1)
    
    time. sleep(3)
        



#This is a function to save all the data retrieved a a Json file.
def SaveJason():    
    a_file = open("data.json", "a", -1, 'utf-8')
    json.dump(post, a_file)
    a_file.close()
    print("File saved successfully")
    print("\n")

    print(">>>>>>>>>>>> HERE IS YOUR FILE <<<<<<<<<<<<\n\n"*5)
    a_file = open("data.json", "r",-1, 'utf-8')
    output = a_file.read()
    print(output)


#This is a function to go down the page.
def GoDown( num):
    webdriver.ActionChains(driver).key_down(Keys.END).perform()
    time.sleep(num/2)




#This is the loop that will help us loop through all the facebook groups, collect the data and save it into our Json file.


for n in  range(len(groupLinks)):
    OpenLink(groupLinks[n], sec)
    time.sleep(3)
    #l = driver.find_elements(By.ID,"mobile_login_bar")
    #s = len(l)
    yy = "Teka somba en ligne is on Facebook."
    try:
        youMust = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/span").text
    except:
        try:
            youMust=""
            loog = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[1]/strong").text
        #print(exceptions.NoSuchElementException("eza te"))
        
        except: 
            loog=""
        #print("Element does not exist")


    #print(youMust + " " + loog)
    if(youMust == "You must log in first." or loog == yy):
        FbLogin(sec)
        time.sleep(3)
        sentence = driver.find_element(By.CLASS_NAME, "_6j_c").text
        if sentence == "Contenu introuvable":   
            print(f"Group Name: {sentence}")
            continue
        
        
        elif sentence != "Contenu introuvable":
            print("Logged in Successfully\n")
            for p in range(sec):
                GoDown(p)
            Collect(sec)
            SaveJason()
            print("successfully scrapped")

    else:
        sentence = driver.find_element(By.CLASS_NAME, "_6j_c").text
        if sentence == "Contenu introuvable":   
            print(f"Group Name: {sentence}")
            continue
        elif sentence != "Contenu introuvable":
            print(">>>Login barrier does not exist <<<")
            time.sleep(2)
            print("\n You can scroll safely")
            GoDown(sec)
            for p in range(sec):
                time.sleep(sec)
                GoDown(p)
            Collect(sec)
            SaveJason()
    print("successfully scrapped")
    



driver.close()  
print("Driver is closed\n")
SaveJason()




##title = "class _4gus "
##state = "_4gut"
##price = "_4guw"

##content="_il"




#open the webpage ( I am using the mobile.facebook because it has less functionalilty so it will be "harder" for facebook bot to track us?!)

