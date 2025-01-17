#!/usr/bin/python3

'''MRUCache module'''

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ Initialize MRUCache
        """
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # If key exists, remove it from access order
                self.access_order.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                # If cache is full, remove the most recently used item
                mru_key = self.access_order.pop(0)
                del self.cache_data[mru_key]
                print("DISCARD: {}".format(mru_key))
            
            # Add the new key and item to the cache
            self.cache_data[key] = item
            self.access_order.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            # Move accessed key to the most recently used position
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
        return None

