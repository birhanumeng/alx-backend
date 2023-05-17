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
        ''' Add key/value pair to cache data.
            If cache is at max capacity (specified by BaseCaching.MAX_ITEMS),
            discard most recently used entry in cache to accommodate new
            entry. '''
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard_item = self.keys.pop()
                del self.cache_data[discard_item]
                print('DISCARD: {}'.format(discard_item))

    def get(self, key):
        """ Get an item by key. """
        if key and key in self.cache_data.keys():
            self.keys.append(self.keys.pop(self.keys.index(key)))
            return self.cache_data[key]
        return None
