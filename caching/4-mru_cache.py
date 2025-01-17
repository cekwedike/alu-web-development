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
                self.access_order.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                mru_key = self.access_order.pop()
                del self.cache_data[mru_key]
                print("DISCARD: {}".format(mru_key))
            self.cache_data[key] = item
            self.access_order.insert(0, key)

    def get(self, key):
        """ Get an item by key
        """
        if key is not None:
            if key in self.cache_data:
                self.access_order.remove(key)
                self.access_order.insert(0, key)
                return self.cache_data[key]
            else:
                return None
