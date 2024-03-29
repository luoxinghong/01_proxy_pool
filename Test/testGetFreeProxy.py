# -*- coding: utf-8 -*-
from ProxyGetter.getFreeProxy import GetFreeProxy
from Config.ConfigGetter import config


def testGetFreeProxy():
    """
    test class GetFreeProxy in ProxyGetter/GetFreeProxy
    :return:
    """
    proxy_getter_functions = config.proxy_getter_functions
    for proxyGetter in proxy_getter_functions:
        proxy_count = 0
        for proxy in getattr(GetFreeProxy, proxyGetter.strip())():
            if proxy:
                print('{func}: fetch proxy {proxy},proxy_count:{proxy_count}'.format(func=proxyGetter, proxy=proxy,
                                                                                     proxy_count=proxy_count))
                proxy_count += 1
        # assert proxy_count >= 20, '{} fetch proxy fail'.format(proxyGetter)


if __name__ == '__main__':
    testGetFreeProxy()
