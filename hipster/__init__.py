#!/usr/bin/python
 # -*- coding: utf-8 -*-

__all__ = ['hipster','config', 'errors']


from hipster import *

@singleton_with_methods
class Hipster():
    API_URL = 'https://api.hipchat.com/v1'
    def __init__(self, token, proxy=None, api_url=None):
        self.AUTH_TOKEN = token
        self.PROXY = proxy
        if api_url:
            self.API_URL = api_url
