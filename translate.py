# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:13:27 2020

@author: Agnieszka
"""

from googletrans import Translator

def main():
    translator = Translator()
    result = translator.translate('Jak się masz?')
    print(result.text)
    
main()