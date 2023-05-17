#!/usr/bin/python3
''' LRU Caching: Create a class LRUCache that inherits from BaseCaching
                 and is a caching system
'''

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    ''' An LRU Cache.
        Inherits all behaviors from BaseCaching except, upon any attempt to
        add an entry to the cache when it is at max capacity (as specified by
        BaseCaching.MAX_ITEMS), it discards the least recently used entry to
        accommodate for the new one.
        Attributes:
          __init__ - method that initializes class instance
          put - method that adds a key/value pair to cache
          get - method that retrieves a key/value pair from cache '''

    def __init__(self):
        ''' Initialize class instance. '''
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in to the cache. When the length of the
            dictionary is greater than BaseCaching.MAX_ITEMS(4),
            the least recently used element is discarded.
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard_key = self.keys.pop(0)
                del self.cache_data[discard_key]
                print("DISCARD: {:s}".format(discard_key))

    def get(self, key):
        ''' Return value stored in `key` key of cache.
            If key is None or does not exist in cache, return None. '''
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            return self.cache_data[key]
        return None
