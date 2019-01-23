import os
import sys
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
import pandas as pd
import numpy as np
import json
# from functools import reduce



def authorize():
    print("authorize start")
    #insert name of  json service account key
    SCOPE = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
    SECRETS_FILE = os.getenv("GOOGLE_SHEETS_CREDENTIALS_FILE",
        "google_secret_key_code@umuzi.org.json")


    # Based on docs here - http://gspread.readthedocs.org/en/latest/oauth2.html
    # Load in the secret JSON key in working directory (must be a service account)
    json_key = json.load(open(SECRETS_FILE))

    # Authenticate using the signed key
    credentials = SignedJwtAssertionCredentials(json_key['client_email'],
                                            json_key['private_key'], SCOPE)
    ret = gspread.authorize(credentials)
    print("authorize end")
    return ret

def fetch_sheet(sheet: str):
    gc = authorize()
    book = gc.open(sheet)
    sheet = book.sheet1 #choose the first sheet
    return pd.DataFrame(sheet.get_all_records())



