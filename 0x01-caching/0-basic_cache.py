#!/usr/bin/env python3
"""Create a caching system module by inherting the BaseCaching class
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Creating caching system class that inherit the BaseCaching
        class.
    """

    def put(self, key, item):
        """ Add an item in the cache. """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key. """
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
