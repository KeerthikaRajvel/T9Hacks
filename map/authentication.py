# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 03:20:52 2020

@author: matth
"""

class authentication:

    def __init__(self):
        # Go to http://apps.twitter.com and create an app
        # The consumer key and secret will be generated for you after
            
        #Twitter Credentials
        self.consumer_key = 'Xsm1PSWiJYFkn0Rmoi53Mm8pU'
        self.consumer_secret = 'DzckZZPyAKPQZdCtUWVshUhczjGMOeST53FmR1q41r2oqOWjuL'
        
        # Create an access token under the "Your access token" section
        self.access_token = '1082567145395937280-10ARA8VBNprf6TzT0o1QDjBojIA9oV'
        self.access_token_secret = '0g84r99NYhYY9Pt69OYKrgr5VeBGh2X6nCAt6oHikdSKO'


    def getconsumer_key(self):
    	return self.consumer_key
    
    def getconsumer_secret(self):
    	return self.consumer_secret
    def getaccess_token(self):
    	return self.access_token
    def getaccess_token_secret(self):
    	return self.access_token_secret
