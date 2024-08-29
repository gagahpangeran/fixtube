from os import environ

CACHE_TYPE = environ.get("CACHE_TYPE", "SimpleCache")
CACHE_DEFAULT_TIMEOUT = int(environ.get("CACHE_DEFAULT_TIMEOUT", "300"))
