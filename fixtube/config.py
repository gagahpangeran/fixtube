from os import environ

APP_VERSION = "2024.09.09"

CACHE_TYPE = environ.get("CACHE_TYPE", "SimpleCache")
CACHE_DEFAULT_TIMEOUT = int(environ.get("CACHE_DEFAULT_TIMEOUT", "300"))

CACHE_REDIS_HOST = environ.get("CACHE_REDIS_HOST")
CACHE_REDIS_PORT = environ.get("CACHE_REDIS_PORT")
CACHE_REDIS_DB = environ.get("CACHE_REDIS_DB")

HOME_PAGE = environ.get("HOME_PAGE", "")
ISSUE_PAGE = environ.get("ISSUE_PAGE", "")
