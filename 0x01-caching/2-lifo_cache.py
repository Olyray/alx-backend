#!/usr/bin/env python3
"""Implementation of LIFO cache replacement policy"""


from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """Implementation of FIFO caching"""
    def __init__(self):
        """Transfers the init from the parent class"""
        super().__init__()

    def put(self, key, item):
        """Inserts item into the cache data"""
        if key is None or item is None:
            return
        copied_cache = self.cache_data.copy()
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.popitem()
            removed_item = self.cache_data.popitem()
            print("DISCARD: {}".format(removed_item[0]))
        if key in copied_cache:
            self.cache_data.pop(key)
            self.cache_data[key] = item
        self.cache_data[key] = item

    def get(self, key):
        """Gets items from the cache data"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
