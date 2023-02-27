# This code doesnt seem to be working need to work out how to best organise getting the access token.
# Currently im logging in to the msft graph api explorer and manually copying the access token

import msal
import requests
import helperBois as hb
config = hb.loadConfig()

# Set up the Microsoft Authentication Library (MSAL) client
client_id = config['client_id']
authority = 'https://login.microsoftonline.com/consumers'
scopes = ['User.Read Calendars.ReadWrite']

app = msal.PublicClientApplication(client_id=client_id, authority=authority)

# Get an access token for the Graph API
result = None
accounts = app.get_accounts()

if accounts:
    result = app.acquire_token_silent(scopes=scopes, account=accounts[0])

if not result:
    result = app.acquire_token_interactive(scopes=scopes)

access_token = result['access_token']

print(access_token)