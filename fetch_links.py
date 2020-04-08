# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 00:21:23 2020

@author: Agnieszka
"""

from bs4 import BeautifulSoup
import urllib.request

def get_content(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    return BeautifulSoup(data, 'html.parser')