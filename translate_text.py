import json
from deep_translator import GoogleTranslator

def load_config():
    with open('config.json', 'r') as file:
        config = json.load(file)
    return config['language']

def translate_text(text, target_language):
    translator = GoogleTranslator(target=target_language)
    translation = translator.translate(text)
    return translation