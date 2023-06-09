#!/usr/bin/env python
""" LRUCache caching system. """

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Implementing LRUCache algorithm by adding key value pairs
        in to a dictionary.
    """
    def __init__(self):
        """ Initiliaze the FIFOCache object. """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in to the cache. When the length of the
            dictionary is greater than BaseCaching.MAX_ITEMS(4),
            the least recently used element is discarded.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """ Get an item by key. """
        if key and key in self.cache_data.keys():
            self.keys.append(self.keys.pop(self.keys.index(key)))
            return self.cache_data[key]
        return None
