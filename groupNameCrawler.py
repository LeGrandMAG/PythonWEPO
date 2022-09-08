
from selenium import webdriver
from selenium.common import  exceptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
##from webdriver_manager.chrome import ChromeDriverManager

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

print(values[1][1])



chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)


#specify the path to chromedriver.exe (download and save on your computer) and launch chrome driver
#driver = webdriver.Chrome('C:/Users/maglo/chromedriver.exe',options=chrome_options)
#wait = WebDriverWait(driver, 2)



"""def FbLogin(num):

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
    print("logged in successfully")
    time.sleep(3)

"""

#driver.get("https://mobile.facebook.com/groups/3966103180150631/")
#FbLogin(3)

#time.sleep(2)



groupLink =  [{'link': 'https://www.facebook.com/groups/3966103180150631/'},
 {'link': 'https://www.facebook.com/groups/162954537532473/'},
 {'link': 'https://www.facebook.com/groups/241523078029097/'},
 {'link': 'https://www.facebook.com/groups/5281764115191912/'},
 {'link': 'https://www.facebook.com/groups/556900801513172/'},
 {'link': 'https://www.facebook.com/groups/199970028622185/'},
 {'link': 'https://www.facebook.com/groups/114868290520926/'},
 {'link': 'https://www.facebook.com/groups/653340472437452/'},
 {'link': 'https://www.facebook.com/groups/3323854697841336/'},
 {'link': 'https://www.facebook.com/groups/672548700534764/'},
 {'link': 'https://www.facebook.com/groups/180494450628005/'},
 {'link': 'https://www.facebook.com/groups/153004319765661/'},
 {'link': 'https://www.facebook.com/groups/3207197752833444/'},
 {'link': 'https://www.facebook.com/groups/3004218809894974/'},
 {'link': 'https://www.facebook.com/groups/2623494271292647/'},
 {'link': 'https://www.facebook.com/groups/1530005517277224/'},
 {'link': 'https://www.facebook.com/groups/1481419625362186/'},
 {'link': 'https://www.facebook.com/groups/237921257324038/'},
 {'link': 'https://www.facebook.com/groups/335538414118390/'},
 {'link': 'https://www.facebook.com/groups/2512061195782681/'},
 {'link': 'https://www.facebook.com/groups/216581003986576/'},
 {'link': 'https://www.facebook.com/groups/222797959913540/'},
 {'link': 'https://www.facebook.com/groups/4458091350904337/'},
 {'link': 'https://www.facebook.com/groups/1440652346351767/'},
 {'link': 'https://www.facebook.com/groups/481026930204042/'},
 {'link': 'https://www.facebook.com/groups/2232354350372325/'},
 {'link': 'https://www.facebook.com/groups/4326455680731929/'},
 {'link': 'https://www.facebook.com/groups/2396795340453227/'},
 {'link': 'https://www.facebook.com/groups/870547810546899/'},
 {'link': 'https://www.facebook.com/groups/1063685117059224/'},
 {'link': 'https://www.facebook.com/groups/3145104845574018/'},
 {'link': 'https://www.facebook.com/groups/1924841527741622/'},
 {'link': 'https://www.facebook.com/groups/1668267026694436/'},
 {'link': 'https://www.facebook.com/groups/1326923207672539/'},
 {'link': 'https://www.facebook.com/groups/1050735792104175/'},
 {'link': 'https://www.facebook.com/groups/988964685032210/'},
 {'link': 'https://www.facebook.com/groups/973184080219760/'},
 {'link': 'https://www.facebook.com/groups/965342120846683/'},
 {'link': 'https://www.facebook.com/groups/959531651331444/'},
 {'link': 'https://www.facebook.com/groups/945704665985070/'},
 {'link': 'https://www.facebook.com/groups/904869436679339/'},
 {'link': 'https://www.facebook.com/groups/855731991501131/'},
 {'link': 'https://www.facebook.com/groups/824817284682260/'},
 {'link': 'https://www.facebook.com/groups/818527738883388/'},
 {'link': 'https://www.facebook.com/groups/814431895688471/'},
 {'link': 'https://www.facebook.com/groups/810087326318921/'},
 {'link': 'https://www.facebook.com/groups/755398911818459/'},
 {'link': 'https://www.facebook.com/groups/708905712627130/'},
 {'link': 'https://www.facebook.com/groups/673810406402554/'},
 {'link': 'https://www.facebook.com/groups/661458215057816/'},
 {'link': 'https://www.facebook.com/groups/651235932668933/'},
 {'link': 'https://www.facebook.com/groups/607221143754265/'},
 {'link': 'https://www.facebook.com/groups/603786827367433/'},
 {'link': 'https://www.facebook.com/groups/601451374497555/'},
 {'link': 'https://www.facebook.com/groups/589906052154278/'},
 {'link': 'https://www.facebook.com/groups/576407803938295/'},
 {'link': 'https://www.facebook.com/groups/537320497314948/'},
 {'link': 'https://www.facebook.com/groups/530901071561693/'},
 {'link': 'https://www.facebook.com/groups/511968929865430/'},
 {'link': 'https://www.facebook.com/groups/510321486475412/'},
 {'link': 'https://www.facebook.com/groups/507311236729344/'},
 {'link': 'https://www.facebook.com/groups/494938151630057/'},
 {'link': 'https://www.facebook.com/groups/BusinessAvenueKennedy/'},
 {'link': 'https://www.facebook.com/groups/452312899465708/'},
 {'link': 'https://www.facebook.com/groups/448757699886602/'},
 {'link': 'https://www.facebook.com/groups/435423051233403/'},
 {'link': 'https://www.facebook.com/groups/433416427691003/'},
 {'link': 'https://www.facebook.com/groups/423593707665319/'},
 {'link': 'https://www.facebook.com/groups/421201913105415/'},
 {'link': 'https://www.facebook.com/groups/409635187484865/'},
 {'link': 'https://www.facebook.com/groups/403108787815568/'},
 {'link': 'https://www.facebook.com/groups/394578501802490/'},
 {'link': 'https://www.facebook.com/groups/353342075612193/'},
 {'link': 'https://www.facebook.com/groups/302541855150147/'},
 {'link': 'https://www.facebook.com/groups/290265768930182/'},
 {'link': 'https://www.facebook.com/groups/278589683717538/'},
 {'link': 'https://www.facebook.com/groups/273882999805184/'},
 {'link': 'https://www.facebook.com/groups/267446018791261/'},
 {'link': 'https://www.facebook.com/groups/265019418581655/'},
 {'link': 'https://www.facebook.com/groups/254663883084070/'},
 {'link': 'https://www.facebook.com/groups/242584221184584/'},
 {'link': 'https://www.facebook.com/groups/241704094385183/'},
 {'link': 'https://www.facebook.com/groups/226033314796476/'},
 {'link': 'https://www.facebook.com/groups/143739249735548/'},
 {'link': 'https://www.facebook.com/groups/114975699094438/'},
 {'link': 'https://www.facebook.com/groups/2932215260333602/'},
 {'link': 'https://www.facebook.com/groups/3095066560726626/'},
 {'link': 'https://www.facebook.com/groups/1305001263300774/'},
 {'link': 'https://www.facebook.com/groups/1113928432436940/'},
 {'link': 'https://www.facebook.com/groups/1106836953180224/'},
 {'link': 'https://www.facebook.com/groups/596912204940042/'},
 {'link': 'https://www.facebook.com/groups/281826390445844/'},
 {'link': 'https://www.facebook.com/groups/322276606448296/'},
 {'link': 'https://www.facebook.com/groups/577166053305561/'},
 {'link': 'https://www.facebook.com/groups/601765924047082/'},
 {'link': 'https://www.facebook.com/groups/440891977563406/'},
 {'link': 'https://www.facebook.com/groups/393809775499534/'},
 {'link': 'https://www.facebook.com/groups/296525075547264/'},
 {'link': 'https://www.facebook.com/groups/2619005908213000/'},
 {'link': 'https://www.facebook.com/groups/434661027871196/'},
 {'link': 'https://www.facebook.com/groups/423828516045341/'},
 {'link': 'https://www.facebook.com/groups/592625602008582/'},
 {'link': 'https://www.facebook.com/groups/1967236646682359/'}]


"""for i in groupLink:
    elem = []
    driver.get(i['link'])
    time.sleep(4)
    link = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div[1]/h1/span/a").get_attribute("href")
    name = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div[1]/h1/span/a").text
    members = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div[2]/span/span/div/div[3]/a").text
    elem.append(name)
    elem.append(link)
    elem.append(members)
    request = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="groupList!A:D", valueInputOption="USER_ENTERED", insertDataOption="INSERT_ROWS", body= {"values":[elem]}).execute()
    print(request)
    time.sleep(1)"""