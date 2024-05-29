# app/ms_translation.py
from googletrans import Translator
import requests

api_key = "d0fd3995752b1b2f813a135042ea3475"

# Define function to detect language
def detect_language(api_key, text):
    url = "https://ws.detectlanguage.com/0.2/detect"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "q": text
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        result = response.json()
        language = result['data']['detections'][0]['language']
        return language
    else:
        return f"Error: {response.status_code}, {response.text}"

# Define function to translate text
def translate_text(input_text, target_language):
    translator = Translator()
    translation = translator.translate(input_text, dest=target_language)
    return translation.text
