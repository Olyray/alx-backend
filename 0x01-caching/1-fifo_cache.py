#!/usr/bin/env python3
"""Implementation of FIFO cache replacement policy"""


from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """Implementation of FIFO caching"""
    def __init__(self):
        """Transfers the init from the parent class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Inserts item into the cache data"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            removed_item = self.cache_data.popitem(last=False)
            print("DISCARD: {}".format(removed_item[0]))

    def get(self, key):
        """Gets items from the cache data"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
