from urllib import request
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
                            range="Sheet1!A:C").execute()
values = result.get('values', [])

AOA= [["Magloirexxxxx", "Welcome to kore"], ["Musa","Thank you for joining us"], ["Go for it", "Alright"]]
#request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet2!A:C", valueInputOption="USER_ENTERED", body={"values":AOA}).execute()
#request = sheet.values().append(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)



def SaveOnGoogleSheet(fbData):  
    #sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet2!A:C", valueInputOption="USER_ENTERED", body={"values":AOA}).execute()
    request = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet1!A:C", valueInputOption="USER_ENTERED", insertDataOption="INSERT_ROWS", body={"values":fbData}).execute()
    print(request)
    

SaveOnGoogleSheet(AOA)