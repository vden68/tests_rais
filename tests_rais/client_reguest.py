# -*- coding: utf-8 -*-

__author__ = 'v.denisov'

import allure
from tests_rais.config_host import ConfigHost as config
from tests_rais.reguest import RegustsHelper as rh

class ClientReguest():
    """
    Проверка
    """

    def __init__(self):
        pass


    @classmethod
    @allure.step('set url_host')
    def set_url_host(self, url_host):
        """

        :param url_host:
        """
        config.url_host = url_host

    @classmethod
    @allure.step('get url_host')
    def get_url_host(self):
        """

        :return: Возращает url хоста
        :rtype: str
        """
        return config.url_host

    @classmethod
    @allure.step('set cookies')
    def set_cookies(self, cookies):
        config.cookies = cookies

    @classmethod
    @allure.step('get cookies')
    def get_cookies(self):
        return config.cookies

    @classmethod
    @allure.step('set headers')
    def set_headers(self, headers):
        config.headers = headers

    @classmethod
    @allure.step('get headers')
    def get_headers(self):
        return config.headers

    @classmethod
    def setting_parameters(cls, url, paths, cookies, headers):
        if isinstance(config.cookies, property):
            config.cookies = None
        if isinstance(config.headers, property):
            config.headers = None
        if url is None:
            url = config.url_host + paths
        else:
            url = url + paths
        if cookies is None:
            cookies = config.cookies
        if headers is None:
            headers = config.headers
        return url, cookies, headers

    @classmethod
    @allure.step('get')
    def get(self, url=None, paths='', cookies=None, params=None, headers=None):
        url, cookies, headers = self.setting_parameters(url, paths, cookies, headers)
        response = rh.get(url=url, cookies=cookies, params=params, headers=headers)
        return response

    @classmethod
    @allure.step('post')
    def post(self, url=None, paths='', cookies=None, data=None, params=None, headers=None, files=None):
        url, cookies, headers = self.setting_parameters(url, paths, cookies, headers)
        response = rh.post(url=url, cookies=cookies, data=data, params=params, headers=headers, files=files)
        return response

    @classmethod
    @allure.step('delete')
    def delete(self, url=None, paths='', cookies=None, data=None, params=None, headers=None, files=None):
        url, cookies, headers = self.setting_parameters(url, paths, cookies, headers)
        response = rh.delete(url=url, cookies=cookies, data=data, params=params, headers=headers, files=files)
        return response

    @classmethod
    @allure.step('options')
    def options(self, url=None, paths='', cookies=None, data=None, params=None, headers=None, files=None):
        url, cookies, headers = self.setting_parameters(url, paths, cookies, headers)
        response = rh.options(url=url, cookies=cookies, data=data, params=params, headers=headers, files=files)
        return response

    @classmethod
    @allure.step('head')
    def head(self, url=None, paths='', cookies=None, data=None, params=None, headers=None, files=None):
        url, cookies, headers = self.setting_parameters(url, paths, cookies, headers)
        response = rh.head(url=url, cookies=cookies, data=data, params=params, headers=headers, files=files)
        return response

    @classmethod
    @allure.step('put')
    def put(self, url=None, paths='', cookies=None, data=None, params=None, headers=None, files=None):
        url, cookies, headers = self.setting_parameters(url, paths, cookies, headers)
        response = rh.put(url=url, cookies=cookies, data=data, params=params, headers=headers, files=files)
        return response

    @classmethod
    @allure.step('patch')
    def patch(self, url=None, paths='', cookies=None, data=None, params=None, headers=None, files=None):
        url, cookies, headers = self.setting_parameters(url, paths, cookies, headers)
        response = rh.patch(url=url, cookies=cookies, data=data, params=params, headers=headers, files=files)
        return response
