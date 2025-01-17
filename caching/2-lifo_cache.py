#!/usr/bin/env python3

'''LIFOCache module'''


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''LIFOCache inherits from BaseCaching and is a
    caching system'''

    def __init__(self):
        '''Initialize LIFOCache'''
        super().__init__()
        self.stack = []

    def put(self, key, item):
        '''Add an item in the cache'''
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                last_item = self.stack.pop()
                del self.cache_data[last_item]
                print('DISCARD: {}'.format(last_item))
            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        '''Get an item by key'''
        if key is not None:
            return self.cache_data.get(key)
