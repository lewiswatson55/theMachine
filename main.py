import helperBois as hb
import NaturalLanguageManager as nlm
import microsoftEmailManager as mem

config = hb.loadConfig()

prompt = input("Enter a prompt: ")
event = nlm.parse_NL(prompt)

print(event)

if event['task'] == 'create':
    mem.create_event(event['event']['start'], event['event']['end'], event['event']['title'])
else:
    print("Task not supported")

