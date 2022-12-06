from selenium import webdriver
from selenium.common import  exceptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from webdriver_manager.chrome import ChromeDriverManager

import time
import json

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '14PXpbLAp3_J3dB8-CCLWIYm8q-RN2JJ5kIZRF7TuJYQ'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Sheet1!A:D").execute()
values = result.get('values', [])

#request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet2!A:C", valueInputOption="USER_ENTERED", body={"values":AOA}).execute()
#request = sheet.values().append(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)




##These are the css class to choose the information
class_name = ["_4gus", "_1-sk", "_4guw", "_4gut", "_5rgt _5nk5 _5msi", "_il"]


articleContainerClass ="//article[@class='_55wo _5rgr _5gh8 async_like']"

#postLinkXPath ="//div/div[1]/a"
#commentXPath = "//footer/div/div[1]/a/div/div[2]/span"
#reactionXPath ="footer/div/div[1]/a/div/div[1]/div"
fbLink = "https://mobile.facebook.com/"

groupLink = [
    {'link': 'https://mobile.facebook.com/groups/3966103180150631/', 'numOfmember': 2334, 'main': 'house', 'lastupdate': '1h'},
    {'link': 'https://mobile.facebook.com/groups/162954537532473/', 'numOfmember': 77139, 'main':'car', 'lastupdate': '1m'},
    {'link': 'https://mobile.facebook.com/groups/556900801513172/', 'numOfmember': 3645, 'main': 'phone', 'lastupdate': '2022.11.21'}, 
    {'link': 'https://mobile.facebook.com/groups/199970028622185/',  'numOfmember': 2839, 'main': 'etc', 'lastupdate': '2022.11.21'},
    {'link': 'https://mobile.facebook.com/groups/114868290520926/', 'numOfmember': 22292, 'main': '?', 'lastupdate': '?'},
    {'link': 'https://mobile.facebook.com/groups/3323854697841336/', 'numOfmember': 59003, 'main': 'phone', 'lastupdate': '5m'},
    {'link': 'https://mobile.facebook.com/groups/672548700534764/', 'numOfmember': 5628, 'main': 'phone', 'lastupdate': '2022.11.11'},
    {'link': 'https://mobile.facebook.com/groups/153004319765661/', 'numOfmember': 997, 'main': 'etc', 'lastupdate': '8h'},
    {'link': 'https://mobile.facebook.com/groups/3207197752833444/', 'numOfmember': 58784, 'main': 'phone', 'lastupdate': '50m'},
    {'link': 'https://mobile.facebook.com/groups/3004218809894974/', 'numOfmember': 3316, 'main': 'etc', 'lastupdate': '16m'},
    {'link': 'https://mobile.facebook.com/groups/2623494271292647/', 'numOfmember': 15090, 'main': 'etc', 'lastupdate': '13h'},
    {'link': 'https://mobile.facebook.com/groups/1530005517277224/', 'numOfmember': 6160, 'main': 'phone', 'lastupdate': '2022.11.17'},
    {'link': 'https://mobile.facebook.com/groups/237921257324038/', 'numOfmember': 5992, 'main': 'etc', 'lastupdate': '12m'},  
    {'link': 'https://mobile.facebook.com/groups/335538414118390/', 'numOfmember': 1514, 'main': 'phone', 'lastupdate': 'just'},  
    {'link': 'https://mobile.facebook.com/groups/216581003986576/', 'numOfmember': 13671, 'main': 'phone', 'lastupdate': '2022.11.11'},  
    {'link': 'https://mobile.facebook.com/groups/4458091350904337/', 'numOfmember': 51914, 'main': 'etc', 'lastupdate': '2022.11.21'},  
    {'link': 'https://mobile.facebook.com/groups/2232354350372325/', 'numOfmember': 7401, 'main': 'etc', 'lastupdate': '22m'},  
    {'link': 'https://mobile.facebook.com/groups/4326455680731929/', 'numOfmember': 18302, 'main': 'phone', 'lastupdate': '2022.10.29'},  
    {'link': 'https://mobile.facebook.com/groups/2396795340453227/', 'numOfmember': 71196, 'main': 'phone', 'lastupdate': '2022.11.11'},  
    {'link': 'https://mobile.facebook.com/groups/870547810546899/', 'numOfmember': 21976, 'main': 'phone', 'lastupdate': '2022.10.13'},  
    {'link': 'https://mobile.facebook.com/groups/1063685117059224/', 'numOfmember': 43325, 'main': 'etc', 'lastupdate': 'just'},  
    {'link': 'https://mobile.facebook.com/groups/1924841527741622/', 'numOfmember': 8308, 'main': 'etc', 'lastupdate': '24min'},  
    {'link': 'https://mobile.facebook.com/groups/1668267026694436/', 'numOfmember': 65814, 'main': 'cloth', 'lastupdate': '2022.04.21'},  
    {'link': 'https://mobile.facebook.com/groups/1326923207672539/', 'numOfmember': 324142, 'main': '?', 'lastupdate': '?'}, ##
    {'link': 'https://mobile.facebook.com/groups/1050735792104175/', 'numOfmember': 2648, 'main': 'etc', 'lastupdate': '10h'},  
    {'link': 'https://mobile.facebook.com/groups/959531651331444/', 'numOfmember': 6324, 'main': 'phone', 'lastupdate': '13h'},  
    {'link': 'https://mobile.facebook.com/groups/945704665985070/', 'numOfmember': 9013, 'main': 'phone', 'lastupdate': '?'},  
    {'link': 'https://mobile.facebook.com/groups/904869436679339/', 'numOfmember': 230, 'main': 'etc', 'lastupdate': '2022.11.20'},  
    {'link': 'https://mobile.facebook.com/groups/855731991501131/', 'numOfmember': 68176, 'main': 'iphone', 'lastupdate': '3h'}, ##
    {'link': 'https://mobile.facebook.com/groups/824817284682260/', 'numOfmember': 29484, 'main': 'phone', 'lastupdate': '?'},  
    {'link': 'https://mobile.facebook.com/groups/814431895688471/', 'numOfmember': 2394, 'main': 'etc', 'lastupdate': '8m'},  
    {'link': 'https://mobile.facebook.com/groups/810087326318921/', 'numOfmember': 81458, 'main': 'phone', 'lastupdate': '?'}, ##
    {'link': 'https://mobile.facebook.com/groups/755398911818459/', 'numOfmember': 2618, 'main': 'etc', 'lastupdate': '11h'},  
    {'link': 'https://mobile.facebook.com/groups/708905712627130/', 'numOfmember': 20456, 'main': 'etc', 'lastupdate': '1h'}, 
    {'link': 'https://mobile.facebook.com/groups/673810406402554/', 'numOfmember': 3255, 'main': 'etc', 'lastupdate': '22h'},  
    {'link': 'https://mobile.facebook.com/groups/661458215057816/', 'numOfmember': 22744, 'main': 'etc', 'lastupdate': '7h'}, 
    {'link': 'https://mobile.facebook.com/groups/607221143754265/', 'numOfmember': 1033, 'main': 'car', 'lastupdate': '1h'},
    {'link': 'https://mobile.facebook.com/groups/603786827367433/', 'numOfmember': 6161, 'main': 'phone', 'lastupdate': '12m'}, 
    {'link': 'https://mobile.facebook.com/groups/589906052154278/', 'numOfmember': 3458, 'main': 'phone', 'lastupdate': '9h'},
    {'link': 'https://mobile.facebook.com/groups/537320497314948/', 'numOfmember': 7916, 'main': 'etc', 'lastupdate': '10m'}, 
    {'link': 'https://mobile.facebook.com/groups/511968929865430/', 'numOfmember': 3636, 'main': 'phone', 'lastupdate': '1h'},
    {'link': 'https://mobile.facebook.com/groups/510321486475412/', 'numOfmember': 3489, 'main': 'etc', 'lastupdate': 'just'},
    {'link': 'https://mobile.facebook.com/groups/507311236729344/', 'numOfmember': 1630, 'main': 'cloth', 'lastupdate': '2022.10.26'},
    {'link': 'https://mobile.facebook.com/groups/BusinessAvenueKennedy/', 'numOfmember': 5450, 'main': 'etc', 'lastupdate': '10h'},  
    {'link': 'https://mobile.facebook.com/groups/452312899465708/', 'numOfmember': 3833, 'main': 'etc', 'lastupdate': '2h'},  
    {'link': 'https://mobile.facebook.com/groups/448757699886602/', 'numOfmember': 4239, 'main': 'phone', 'lastupdate': '32min'},  
    {'link': 'https://mobile.facebook.com/groups/435423051233403/', 'numOfmember': 3968, 'main': 'cloth', 'lastupdate': '?'},  
    {'link': 'https://mobile.facebook.com/groups/433416427691003/', 'numOfmember': 34899, 'main': 'community', 'lastupdate': '3h'}, 
    {'link': 'https://mobile.facebook.com/groups/423593707665319/', 'numOfmember': 4669, 'main': 'etc', 'lastupdate': '3h'}, 
    {'link': 'https://mobile.facebook.com/groups/421201913105415/', 'numOfmember': 9140, 'main': 'phone', 'lastupdate': '11m'},  
    {'link': 'https://mobile.facebook.com/groups/409635187484865/', 'numOfmember': 3904, 'main': 'phone', 'lastupdate': '17h'},  
    {'link': 'https://mobile.facebook.com/groups/403108787815568/', 'numOfmember': 9759, 'main': 'camera', 'lastupdate': '2022.10.27'},  
    {'link': 'https://mobile.facebook.com/groups/302541855150147/', 'numOfmember': 7641, 'main': 'phone', 'lastupdate': '?'},  
    {'link': 'https://mobile.facebook.com/groups/278589683717538/', 'numOfmember': 735, 'main': 'phone', 'lastupdate': '2022.11.21'},  
    {'link': 'https://mobile.facebook.com/groups/273882999805184/', 'numOfmember': 11404, 'main': 'community', 'lastupdate': '10h'},  
    {'link': 'https://mobile.facebook.com/groups/265019418581655/', 'numOfmember': 3145, 'main': 'phone', 'lastupdate': '?'},  
    {'link': 'https://mobile.facebook.com/groups/242584221184584/', 'numOfmember': 7727, 'main': 'etc', 'lastupdate': '2022.11.7'},
    {'link': 'https://mobile.facebook.com/groups/241704094385183/', 'numOfmember': 21712, 'main': 'notebook', 'lastupdate': '18h'},
    {'link': 'https://mobile.facebook.com/groups/143739249735548/', 'numOfmember': 2513, 'main': 'e-commerce', 'lastupdate': '2022.10.27'},  
    {'link': 'https://mobile.facebook.com/groups/114975699094438/', 'numOfmember': 18486, 'main': 'etc', 'lastupdate': '6h'},
    {'link': 'https://mobile.facebook.com/groups/2932215260333602/', 'numOfmember': 92203, 'main': 'phone', 'lastupdate': '41m'}, ##
    {'link': 'https://mobile.facebook.com/groups/3095066560726626/', 'numOfmember': 25054, 'main': 'phone', 'lastupdate': '12h'}, 
    {'link': 'https://mobile.facebook.com/groups/1305001263300774/', 'numOfmember': 20502, 'main': 'phone', 'lastupdate': '2022.8.25'},  
    {'link': 'https://mobile.facebook.com/groups/1113928432436940/', 'numOfmember': 7256, 'main': 'phone', 'lastupdate': '3m'},  
    {'link': 'https://mobile.facebook.com/groups/596912204940042/', 'numOfmember': 19485, 'main': 'phone', 'lastupdate': '2022.11.2'}, 
    {'link': 'https://mobile.facebook.com/groups/281826390445844/', 'numOfmember': 6752, 'main': 'phone', 'lastupdate': '16m'},  
    {'link': 'https://mobile.facebook.com/groups/322276606448296/', 'numOfmember': 43501, 'main': 'phone', 'lastupdate': '2022.8.10'}, 
    {'link': 'https://mobile.facebook.com/groups/577166053305561/', 'numOfmember': 13546, 'main': 'gameconsole', 'lastupdate': '2022.11.16'},  
    {'link': 'https://mobile.facebook.com/groups/440891977563406/', 'numOfmember': 11939, 'main': 'phone', 'lastupdate': '2022.10.31'}, 
    {'link': 'https://mobile.facebook.com/groups/393809775499534/', 'numOfmember': 1852, 'main': 'etc', 'lastupdate': '8h'}, 
    {'link': 'https://mobile.facebook.com/groups/296525075547264/', 'numOfmember': 19626, 'main': 'phone', 'lastupdate': '1h'},
    {'link': 'https://mobile.facebook.com/groups/2619005908213000/', 'numOfmember': 1876, 'main': 'etc', 'lastupdate': '21h'},  
    {'link': 'https://mobile.facebook.com/groups/434661027871196/', 'numOfmember': 39214, 'main': 'phone', 'lastupdate': '1d'},  
    {'link': 'https://mobile.facebook.com/groups/592625602008582/', 'numOfmember': 36665, 'main': 'phone', 'lastupdate': '1h'},  
    {'link': 'https://mobile.facebook.com/groups/1967236646682359/', 'numOfmember': 12710, 'main': 'etc', 'lastupdate': '2022.11.21'}
 ]

sec= int(input("input the processing time: "))
scroll=int(input("input the number of time you want to scroll: "))

words=[]
#listnum = int(input("How many word in the list: "))

        
#Set up the Chrome options

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

#specify the path to chromedriver.exe (download and save on your computer) and launch chrome driver
driver = webdriver.Chrome('C:/Users/KING-K-S/pythonWEPO/pythonWEPO/chromedriver.exe',options=chrome_options)
# driver = webdriver.Chrome('C:/Users/maglo/chromedriver.exe',options=chrome_options)3
wait = WebDriverWait(driver, 2)


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
    username.send_keys("kookdo88@naver.com")
    password.clear()
    password.send_keys("4674470qwe!")

    driver.implicitly_wait(num)
    #target the login button and click it
    button = WebDriverWait(driver, num).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='button']"))).click()
    
    # if facebook want verify your account
    # WebDriverWait(driver, num).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkpointSubmitButton-actual-button'))).click()
    # WebDriverWait(driver, num).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkpointSubmitButton-actual-button'))).click()
    
    # birthday_captcha_year = WebDriverWait(driver, num).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='birthday_captcha_year']")))
    # birthday_captcha_month = WebDriverWait(driver, num).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='birthday_captcha_month']")))
    # birthday_captcha_day = WebDriverWait(driver, num).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='birthday_captcha_day']")))
    
    # birthday_captcha_year.clear()
    # birthday_captcha_year.send_key('1988')
    # birthday_captcha_month.clear()
    # birthday_captcha_month.send_key('12')
    # birthday_captcha_day.clear()
    # birthday_captcha_day.send_key('28')
    
    # WebDriverWait(driver, num).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkpointSubmitButton-actual-button'))).click()
    
    
    
postContentClass =[]

print("Now collecting the data", end="")
for e in range(3):
    print('.', end="")
    time.sleep(2)
print('\n')


#This is a function to collect data
def Collect(r, t):
    post = []
    action_chain = webdriver.ActionChains(driver)
    refresh = driver.refresh()
    print("\n")
    time.sleep(3)

    # A Loop to scroll at the bottom of the page
    for a in range(t):
        action_chain.key_down(Keys.END).perform()
        print(str(a) + " scroll")
        time.sleep(3)
    print("\n")
    # This is the variable for list of articles we are going to retrieve. 
    listOfArticles = driver.find_elements(By.XPATH, articleContainerClass)    
    #This is a for loop to collect data from every single articles.
    for i in listOfArticles:
        
        #Here we will retrieve the name of the seller, the post content and the post link
        post = []
        postArray = []
    #print(i)
        l = i.find_elements(By.CLASS_NAME, "story_body_container")
        
        # Check if it is a shared post or it was posted directly on the group.
        if(len(l) ==2):

            #If it is a shared post
            sellerName = l[1].find_element(By.XPATH,".//strong").text
            postDetail = l[1].find_element(By.XPATH,".//div[@class='_5rgt _5nk5 _5msi']").text
            postLink = l[1].find_element(By.XPATH,".//a[@class='_5msj']").get_attribute("href")

        elif(len(l)==1):
            # If it was not shared

            sellerName = l[0].find_element(By.XPATH,".//strong").text
            postDetail = l[0].find_element(By.XPATH,".//div[@class='_5rgt _5nk5 _5msi']").text
            postLink = l[0].find_element(By.XPATH,".//a[@class='_5msj']").get_attribute("href")
        else:
            postLink = "No link"
        #Let's shorten the post link 
        numberOfSlash = 0
        temp = []

        if postLink!= "No link":
            for t in postLink:

                if numberOfSlash ==7:
                    break
                if t =="/":
                    numberOfSlash += 1
                temp.append(t)
            if "https://m" in postLink:
                postLink = "".join(temp)
            else:
                postLink = "https://mobile.facebook.com" + "".join(temp)


        # We will save the retrieved data into the post object and save it in our list.
        exist = False
        #check if the link already exist in the list of posts from the google sheet
        for l in range(len(values)-2):
                print(f"{l}\n")
                if postLink == values[l][2] and postDetail == values[l][1]:
                    print(f"{values[l][2]} already exists")

                    exist = True
                    break
        #check if it exist in the temporary list of posts.
        if exist==False:
            for x in post:
                if postLink == x[2] and postDetail == x[1]:
                    print(f"{x[2]} already exists")
                    exist = True
                    break
        #add the post to the temporary lists
        if(len(postDetail)>0 and exist == False ):    
            postArray.append(sellerName)
            postArray.append(postDetail)
            postArray.append(postLink)
            # print the collected Data to the console
            #print("Seller Name: " + sellerName)
            #print("POST CONTENT\n==== ======\n\n" + postDetail + "\n")
            #print("Post Link: " + postLink + "\n" )
            #print(postArray)
            post.append(postArray)
            print(f"This temporary post list has: {len(post)} posts")
            SaveOnGoogleSheet(post)
            time.sleep(0.5)

            print("\n === The post was added to the list of data to be saved ===\n")

        # If the post is empty, we will return an empty object
        elif exist == True and postDetail == "" or len(postDetail)==0:
            continue
            
    print("----------------------")
    print("\n")

    #IF the post is not empty add it in the google drive.

#This is a function to save all the data retrieved a a Json file.
def SaveOnGoogleSheet(fbData):  
    #sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet2!A:C", valueInputOption="USER_ENTERED", body={"values":AOA}).execute()
    request = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet1!A:C", valueInputOption="USER_ENTERED", insertDataOption="INSERT_ROWS", body={"values":fbData}).execute()
    print(request)
    print(request)
    print("=== This saved on google sheet ===\n")


#This is a function to go down the page.
def GoDown( num):
    webdriver.ActionChains(driver).key_down(Keys.END).perform()
    time.sleep(3)


#This is the loop that will help us loop through all the facebook groups, collect the data and save it into our Json file.
# n_iteration = len(groupLink)-1
OpenLink(groupLink[0]['link'], sec)
FbLogin(sec)
time.sleep(3)

n_iteration = 10
for n in  range(n_iteration):
    OpenLink(groupLink[n]['link'], sec)
    time.sleep(3)
    # l = driver.find_elements(By.ID,"mobile_login_bar")
    # s = len(l)
    yy = "Teka somba en ligne is on Facebook."
    try:
        youMust = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/span").text
        print(youMust)
    except:
        try:
            youMust=""
            loog = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div[2]/div[1]/div[1]/strong").text
        #print(exceptions.NoSuchElementException("eza te"))
        
        except: 
            loog=""
        #print("Element does not exist")

    #print(youMust + " " + loog)
    # if(youMust == "You must log in first." or "먼저 로그인하세요." or yy in loog):
    
    # if(youMust == "You must log in first." or "먼저 로그인하세요."):
    #     FbLogin(sec)
    #     time.sleep(3)
    #     try:
    #         sentence = driver.find_element(By.CLASS_NAME, "_6j_c").text
    #     except:
    #         sentence= "error"
    #         driver.refresh()
    #     if sentence == "Contenu introuvable":   
    #         print(f"Group Name: {sentence}")
    #         continue
        
        
    #     elif sentence != "Contenu introuvable":
    #         print("Logged in Successfully\n")
    #         for p in range(sec):
    #             GoDown(p)
    #         Collect(sec,scroll)

    # else:
    try:
        sentence = driver.find_element(By.CLASS_NAME, "_6j_c").text
    except:
        continue
    if sentence == "Contenu introuvable":   
        #print(f"Group Name: {sentence}")
        continue
    elif sentence != "Contenu introuvable":
        print(">>>Login barrier does not exist <<<\n")
        print("\n You can scroll safely\n")
        GoDown(sec)
        for p in range(sec):
            time.sleep(sec)
            GoDown(p)
        Collect(sec,scroll)
    time.sleep(2)


driver.close()  
print("Driver is closed\n")


#open the webpage ( I am using the mobile.facebook because it has less functionalilty so it will be "harder" for facebook bot to track us?!)

