import sys
import requests
import json
import logging
import time
from user_details.models import AuthTokens



test_api_url = "http://127.0.0.1:8000"

##
##    function to obtain a new OAuth 2.0 token from the authentication server
##
def get_new_token():

    import requests
    import json

    

    # url ="https://accounts.google.com/o/oauth2/v2/auth?response_type=code&prompt=consent&access_type=offline&code&client_id=650284881740-ogi5cv7h4n7qk5utoorkoq2mbmho4kh4.apps.googleusercontent.com&redirect_uri=http://127.0.0.1:8000&scope=https://www.googleapis.com/auth/calendar&state=1234"

    # response = requests.request("GET", url)

    # print(response.text)



    refresh="1//0g4fnJhtxZutTCgYIARAAGBASNwF-L9IrdgiMGr-r5vjjEQaN84sj4RwZYweHDb5VJS0sqkKbm6ZaVyEHL-WJHKyaxjhpOp0qdtA"


    url = "https://oauth2.googleapis.com/token"

    payload = json.dumps({
    "grant_type": "refresh_token",
    "refresh_token": refresh,
    "redirect_uri": "http://127.0.0.1:8000",
    "client_id": "650284881740-ogi5cv7h4n7qk5utoorkoq2mbmho4kh4.apps.googleusercontent.com",
    "client_secret": "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"
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.json())
    res=response.json()
    # AuthTokens.objects.create(token1=res['access_token'])
    AuthTokens.objects.filter(id=1).update(token1=res['access_token'])
    print('statsussss',response.status_code)
    return res


    
## 
## 	obtain a token before calling the API for the first time
##
# token = get_new_token()

# while True:

##
##   call the API with the token
##
# api_call_headers = {'Authorization': 'Bearer ' + token}
# api_call_response = requests.get(test_api_url, headers=api_call_headers, verify+False)

##
##
# if	api_call_response.status_code == 401:
# 			token = get_new_token()
# else:
#     print(api_call_response.text)








# import datetime
# import os.path

# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError

# # If modifying these scopes, delete the file token.json.
# SCOPES = ["https://www.googleapis.com/auth/calendar"]


# def main():
#   """Shows basic usage of the Google Calendar API.
#   Prints the start and name of the next 10 events on the user's calendar.
#   """
#   creds = None
#   # The file token.json stores the user's access and refresh tokens, and is
#   # created automatically when the authorization flow completes for the first
#   # time.
#   if os.path.exists("token.json"):
#     creds = Credentials.from_authorized_user_file("token.json", SCOPES)
#   # If there are no (valid) credentials available, let the user log in.
#   if not creds or not creds.valid:
#     if creds and creds.expired and creds.refresh_token:
#       creds.refresh(Request())
#     else:
#       flow = InstalledAppFlow.from_client_secrets_file(
#           "credentials.json", SCOPES
#       )
#       creds = flow.run_local_server(port=0)
#     # Save the credentials for the next run
#     with open("token.json", "w") as token:
#       token.write(creds.to_json())

#   try:
#     service = build("calendar", "v3", credentials=creds)

#     # Call the Calendar API
#     now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
#     print("Getting the upcoming 10 events")
#     events_result = (
#         service.events()
#         .list(
#             calendarId="primary",
#             timeMin=now,
#             maxResults=10,
#             singleEvents=True,
#             orderBy="startTime",
#         )
#         .execute()
#     )
#     events = events_result.get("items", [])

#     if not events:
#       print("No upcoming events found.")
#       return

#     # Prints the start and name of the next 10 events
#     for event in events:
#       start = event["start"].get("dateTime", event["start"].get("date"))
#       print(start, event["summary"])

#   except HttpError as error:
#     print(f"An error occurred: {error}")


# if __name__ == "__main__":
#   main()