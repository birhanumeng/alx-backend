#!/usr/bin/env python
""" FIFO caching system. """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(.BaseCaching):
    """ Implementing FIFO algorithm by adding key value pairs
        in to a dictionary. When the length of the dictionary
        is greater than BaseCaching.MAX_ITEMS(4), the first
        inserted element is discarded.
    """
    def __init(self):
        """ Initiliaze the FIFOCache object. """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache. When the length of the dictionary
            is greater than BaseCaching.MAX_ITEMS(4), the first inserted
            element is discarded.
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard_key = self.keys.pop(0)
                del self.cache_data[discard_key]
                print("DISCARD: {:s}".format(discard_key))

    def get(self, key):
        """ Get an item by key. """
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
