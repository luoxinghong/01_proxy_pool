# -*- coding: utf-8 -*-
import sys
from os import getenv
from logging import getLogger
log = getLogger(__name__)


PY3 = sys.version_info >= (3,)



DB_TYPE = getenv('db_type', 'redis').upper()
DB_HOST = getenv('db_host', '127.0.0.1')
DB_PORT = getenv('db_port', '6379')
DB_PASSWORD = getenv('db_password', 'lxh123')

DATABASES = {
    "default": {
        "TYPE": DB_TYPE,
        "HOST": DB_HOST,
        "PORT": DB_PORT,
        "NAME": "proxy",
        "PASSWORD": DB_PASSWORD
    }
}

PROXY_GETTER = [
    "freeProxy01",
    "freeProxy02",
    "freeProxy03",
    "freeProxy04",
    "freeProxy05",
    "freeProxy06",
    "freeProxy07",
    "freeProxy08",
    "freeProxy09",
]

""" 配置 API服务 http://127.0.0.1:5010 """
SERVER_API = {
    "HOST": "127.0.0.1",
    "PORT": 5010
}


class ConfigError(BaseException):
    pass


def checkConfig():
    if DB_TYPE not in ["SSDB", "REDIS"]:
        raise ConfigError('db_type Do not support: %s, must SSDB/REDIS .' % DB_TYPE)

    if not DB_PORT.isdigit():
        raise ConfigError('db_port must be digit, not %s' % DB_PORT)

    from ProxyGetter import getFreeProxy
    illegal_getter = list(filter(lambda key: not hasattr(getFreeProxy.GetFreeProxy, key), PROXY_GETTER))
    if len(illegal_getter) > 0:
        raise ConfigError("ProxyGetter: %s does not exists" % "/".join(illegal_getter))


checkConfig()
