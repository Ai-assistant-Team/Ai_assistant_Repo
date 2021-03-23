# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 06:11:25 2021

@author: Θόδωρος
"""

def googleMapsSearch(query=""):
    ## If called with a parameter, it opens a google maps page and searches for the given text
    ## If called without a parameter, it opens a google maps page, with an empty search bar
    
    from openUrls import openUrl
    
    from urllib.parse import urlencode, quote_plus              # import the parts of the urllib.parse that are needed 


    url_base = "https://www.google.com/maps/search/?api=1"      # this is the url that leads to google maps search
    
    payload = {"query" : query}                                 # before it gets transformed into a url form, the payload must first be written as a dictionary. (The payload contains the search parameters)
    
    url_form_payload = urlencode(payload, quote_via=quote_plus) # convert the dictionary into url-compatible form

    final = url_base + "&" + url_form_payload                   # concatenate the url_base with the, url-compatible, payload (a '&' is needed in between)
    
    openUrl(final)                                              # opens the final url in a Web Browser




def test():
    ## Used only for testing the code
    googleMapsSearch(input("What would you like to search?\n"))
    googleMapsSearch()                                          # when used without parameters, it opens google maps empty search 
    
    
test()