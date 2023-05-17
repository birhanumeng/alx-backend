#!/usr/bin/env python3
"""Create a caching system module by inherting the BaseCaching class
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Creating caching system class that inherit the BaseCaching
        class.
    """
    def __init__(self):
        """ Initiliazing the objects. """
        super(self)

    def put(self, key, item):
        """ Add an item in the cache. """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key. """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
