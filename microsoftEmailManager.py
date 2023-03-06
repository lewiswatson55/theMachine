import helperBois as hb

config = hb.loadConfig()
access_token = config['access_token']


def viewEvent(event):
    import requests

    # Set up the Graph API endpoint and query parameters
    url = 'https://graph.microsoft.com/v1.0/me/calendar/events'
    #url = 'https://graph.microsoft.com/v1.0/users'
    params = {
        '$select': 'subject,start,end',
        '$orderby': 'start/dateTime desc',
        '$top': 10
    }

    # Set the Authorization header to include the access token
    headers = {
        'Authorization': 'Bearer ' + access_token
    }

    # Make the API call and parse the JSON response
    response = requests.get(url, headers=headers, params=params)
    print(response.json())
    events = response.json()['value']
    for event in events:
        print(event['subject'], event['start']['dateTime'], event['end']['dateTime'])

import requests
import json
import datetime

def create_event(start_time, end_time, title):
    # Set up authentication and headers
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }

    # Set up the data for the new event
    event_data = {
        'subject': title,
        'start': {
            'dateTime': start_time,
            'timeZone': 'UTC'
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'UTC'
        }
    }

    # Make a POST request to create the event
    create_event_url = 'https://graph.microsoft.com/v1.0/me/events'
    response = requests.post(create_event_url, headers=headers, data=json.dumps(event_data))

    # Check for errors and return the event ID if successful
    if response.status_code == 201:
        event_id = response.json()['id']
        return event_id
    else:
        raise Exception('Error creating event: ' + response.text)
