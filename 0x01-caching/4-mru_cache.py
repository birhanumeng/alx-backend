#!/usr/bin/env python
""" MRUCache caching system. """

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ Implementing MRUCache algorithm by adding key value pairs
        in to a dictionary.
    """
    def __init__(self):
        """ Initiliaze the MRUCache object. """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in to the cache. When the length of the
            dictionary is greater than BaseCaching.MAX_ITEMS(4),
            the most recently used element is discarded.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard_item = self.keys.pop(-2)
                del self.cache_data[discard_item]
                print('DISCARD: {}'.format(discard_item))

    def get(self, key):
        """ Get an item by key. """
        if key and key in self.cache_data.keys():
            self.keys.append(self.keys.pop(self.keys.index(key)))
            return self.cache_data[key]
        return None
