# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 00:21:23 2020

@author: Agnieszka
"""

from bs4 import BeautifulSoup
import urllib.request

def main():
    user_url = input("Paste your url here: \n")
    print("Processing...") 
    content = get_content(user_url)
        
    lists = content.find_all('ol')
    
    for i in range(len(lists)):
        elements = lists[i].find_all('li')
        print("List number {}".format(i+1))
        for j in range(len(elements)):
            print("\t{}) {}".format(j+1, elements[j].get_text())) 
    
    return

def get_content(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    return BeautifulSoup(data, 'html.parser')

main()