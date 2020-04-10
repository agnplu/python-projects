# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:13:27 2020

@author: Agnieszka
"""

from googletrans import Translator
import requests
import json

def googletrans():
    translator = Translator()
    result = translator.translate('Jak się masz?', dest = 'es')
    print(result.text)
    
def piratetrans(text):
    url = 'https://api.funtranslations.com/translate/pirate.json'
    data = {'text': text}
    
    response = requests.post(url, data = data)
    json_data = json.loads(response.text)
    print(type(json_data))
    print(json_data['contents'] ['translated'])
    
piratetrans('What are you going to eat?')