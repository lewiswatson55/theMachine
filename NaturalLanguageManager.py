import code
import json
import openai
import helperBois as hb

config = hb.loadConfig()  # Load the config file
openai.api_key = config['openai_key']  # replace with your API key

preprompt = "You are the interface for a calendar, you must parse the user's input into a json object in the form: {\"task\": \"1\",\"event\": {\"start\": \"2023-03-01T09:00:00\",\"end\": \"2023-03-01T11:00:00\",\"title\": \"Team meeting\"}} and return it. You must reason from the user's input as to what task is being completed: create, delete, edit, unknown (event title should default to: UNKNOWN). And you must reason what the data to be entered to the JSON object is. The current year is 2023, today is the 28th of feb. You will not make time assumptions, if no time from the user assume all day You will only return the JSON and nothing else.\nUser:"

def parse_NL(prompt):
    # Call OpenAI's GPT-3 model to generate text
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=preprompt+prompt,
        max_tokens=1024,
        temperature=0.5,
    )

    # Extract the generated text from the API response
    text = response.choices[0].text.strip()

    # Return json object
    return json.loads(text)


# Dummy code for dentist appointment returns string of JSON
def dummyJSON():
    return "{\"task\": \"create\", \"event\": {\"start\": \"2023-01-05T00:00:00\", \"end\": \"2023-01-05T23:59:59\", \"title\": \"Go to the dentist\"}}"

# Test
#event = parse_NL("I need to go to the dentist on the 5th of January")
# event = dummyJSON()
#
# # Parse JSON from string
# event = json.loads(event)
#
# print(event)
