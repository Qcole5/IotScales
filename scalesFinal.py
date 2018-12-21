import json
import sys
import time
import datetime

import gspread
from oauth2client.service_account import ServiceAccountCredentials

import smbus

GDOCS_OAUTH_JSON = 'client_secret2.json'
GDOCS_SPREADSHEET_NAME = 'Pi Test'

FREQUENCY_SECONDS = 2

def login_open_sheet(oauth_key_file, spreadsheet):
    """Connect to Google Docs spreadsheet and return the first worksheet."""
    try:
        scope =  ['https://spreadsheets.google.com/feeds',
                  'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(oauth_key_file, scope)
        gc = gspread.authorize(credentials)
        worksheet = gc.open(spreadsheet).sheet1
        return worksheet
    except Exception as ex:
        print('Unable to login and get spreadsheet.  Check OAuth credentials, spreadsheet name, and make sure spreadsheet is shared to the client_email address in the OAuth .json file!')
        print('Google sheet login failed with error:', ex)
        sys.exit(1)
        

print('Logging scale measurements to {0}.'.format(GDOCS_SPREADSHEET_NAME))
print('Press Ctrl-C to quit.')
worksheet = None

row = 1
collumn = 1
num = 1

while True:
    # Login if necessary.
    if worksheet is None:
        worksheet = login_open_sheet(GDOCS_OAUTH_JSON, GDOCS_SPREADSHEET_NAME)

    try:
        worksheet.update_cell(row,collumn,num)
    except:
        # Error appending data, most likely because credentials are stale.
        # Null out the worksheet so a login is performed at the top of the loop.
        print('Append error, logging in again')
        worksheet = None
        time.sleep(FREQUENCY_SECONDS)
        continue

    row += 1
   #collumn += 1
    num += 1

    # Wait 2 seconds before continuing
    print('Wrote a row to {0}'.format(GDOCS_SPREADSHEET_NAME))
    time.sleep(FREQUENCY_SECONDS)

