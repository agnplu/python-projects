# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 13:42:30 2020

@author: Agnieszka
"""

import urllib.request
from bs4 import BeautifulSoup
import urllib.parse

def main():
    print('Getting staff urls...')
    
    staff_url = 'http://wa.amu.edu.pl/wa/en/staff_list'
    staff_content = get_content(staff_url)
    
    links = staff_content.find_all('a')
    
    urls = []
    
    for link in links:
        if len(link.get_text()) > 1:
            base_url = 'http://wa.amu.edu.pl'
            url = urllib.parse.urljoin(base_url, link['href'])
            encoded_url = fix_encoding(url)
            urls.append(encoded_url)
            
    print('Staff headers found: ')
    for url in urls:
        print(get_details(url))
        
def fix_encoding(url):
    components = urllib.parse.urlsplit(url)
    components = list(components)
    components[2] = urllib.parse.quote(components[2])
    return urllib.parse.urlunsplit(components)

def get_content(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    doc = BeautifulSoup(data, 'html.parser')
    return doc.find(id = 'tresc_wlasciwa')

def get_details(url):
    try:
        content = get_content(url)
    except:
        print('Error getting details from', url)
        return 'no content'
    header = content.find('h1')
    links = content.find_all('a')
    for link in links:
        if link.has_attr('href') and link['href'].startswith('mailto:'):
            email = link.get_text()
            return header.get_text() + ': ' + email
    return header.get_text() + '(no email found)'
    
main()