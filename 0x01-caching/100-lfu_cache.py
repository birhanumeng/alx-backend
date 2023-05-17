#!/usr/bin/env python
""" LFUCache caching system. """

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ Implementing LFUCache algorithm by adding key value pairs
        in to a dictionary.
    """
    def __init__(self):
        """ Initiliaze the LFUCache object. """
        super().__init__()
        self.keys = []
        self.num_ref = {}

    def put(self, key, item):
        """ Add an item in to the cache. When the length of the
            dictionary is greater than BaseCaching.MAX_ITEMS(4),
            the least frequentcy used element is discarded. If
            there are more than one elements to be deleted, use
            least recently used (LRU) algorithm to decide which
            will be delete.
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
                self.num_ref[key] = 1
            else:
                self.num_ref[key] = self.num_ref[key] + 1
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                lfu = min(list(self.num_ref.values()))
                dis = [k for k, v in self.num_ref.items() if v == lfu][0]
                del self.cache_data[dis]
                print("DISCARD: {}".format(dis))

    def get(self, key):
        """ Get an item by key. """
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
