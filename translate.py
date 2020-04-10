# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:13:27 2020

@author: Agnieszka
"""

from googletrans import Translator
import requests

def googletrans():
    translator = Translator()
    result = translator.translate('Jak się masz?')
    print(result.text)
    
def piratetrans(text):
    url = 'https://api.funtranslations.com/translate/pirate.json'
    data = {'text': text}
    
    response = requests.post(url, data = data)
    print(response.text)
    
piratetrans('Hello, sir')