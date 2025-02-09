import os
import json

if not os.path.exists('config.json'):
    TOKEN = input("Veuillez entrer le token du bot : ")
    OPENROUTER_API_KEY = input("Veuillez entrer la clé API OpenRouter : ")
    with open('config.json', 'w') as f:
        json.dump({
            "token": TOKEN,
            "openrouter_api_key": OPENROUTER_API_KEY,
        }, f)
else:
    with open('config.json', 'r') as f:
        config = json.load(f)
        TOKEN = config['token']
        OPENROUTER_API_KEY = config['openrouter_api_key']
