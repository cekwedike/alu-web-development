#!/usr/bin/env python3

"""A basic dictionary"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    No limit
    """

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """retrieve an item form the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
