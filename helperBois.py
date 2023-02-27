import json

import msal


def loadConfig():
    # Load config from config.json
    with open('config.json') as f:
        secrets = json.load(f)
    return secrets
