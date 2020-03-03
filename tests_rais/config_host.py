__author__ = 'v.denisov'

import allure
from tests_rais.reguest import RegustsHelper as rh


class ConfigHost():

    def __init__(self):
        self._url_host = None
        self._cookies = None
        self._headers = None

    @property
    def url_host(self):
        return self._url_host

    @url_host.setter
    def set_url_host(self, value):
        self._url_host = value

    @property
    def cookies(self):
        return self._cookies

    @cookies.setter
    def set_cookies(self, value):
        self._cookies = value

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def set_headers(self, value):
        self._headers = value
