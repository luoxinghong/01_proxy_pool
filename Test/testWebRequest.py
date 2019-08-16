# -*- coding: utf-8 -*-
from Util.WebRequest import WebRequest


# noinspection PyPep8Naming
def testWebRequest():
    """
    test class WebRequest in Util/WebRequest.py
    :return:
    """
    wr = WebRequest()
    request_object = wr.get('https://www.baidu.com/')
    print(request_object)


if __name__ == '__main__':
    testWebRequest()
