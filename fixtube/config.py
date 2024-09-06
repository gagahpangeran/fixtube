from os import environ

APP_VERSION = "2024.09.07"

CACHE_TYPE = environ.get("CACHE_TYPE", "SimpleCache")
CACHE_DEFAULT_TIMEOUT = int(environ.get("CACHE_DEFAULT_TIMEOUT", "300"))

HOME_PAGE = environ.get("HOME_PAGE", "")
ISSUE_PAGE = environ.get("ISSUE_PAGE", "")
