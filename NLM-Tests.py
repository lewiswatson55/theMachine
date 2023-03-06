import NaturalLanguageManager as nlm
import helperBois as hb

config = hb.loadConfig()

prompt = input("Enter a prompt: ")
event = nlm.parse_NL(prompt)

print(event)