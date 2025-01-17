#!/usr/bin/env python3

'''FIFOCache module'''


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''
    FIFOCache inherits from BaseCaching and is a caching system
    '''
    def __init__(self):
        '''Initialize FIFOCache'''
        super().__init__()
        self.queue = []

    def put(self, key, item):
        '''Add an item in the queue'''
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                first_item = self.queue.pop(0)
                del self.cache_data[first_item]
                print("DISCARD: {}".format(first_item))
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        '''Get an item by key'''
        if key is not None:
            return self.cache_data.get(key)
