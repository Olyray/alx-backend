#!/usr/bin/env python3
"""Implementation of LRU cache replacement policy"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Implementation of FIFO caching"""
    def __init__(self):
        """Transfers the init from the parent class"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Inserts item into the cache data"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.queue.remove(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            deleted_key = self.queue.pop(0)
            del self.cache_data[deleted_key]
            print("DISCARD: {}".format(deleted_key))
        self.queue.append(key)

    def get(self, key):
        """Gets items from the cache data"""
        if key is None or key not in self.cache_data:
            return None
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache_data[key]
