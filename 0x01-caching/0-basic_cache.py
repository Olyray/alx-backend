#!/usr/bin/env python3
"""
Creates a class BasicCache that inherits from BaseCaching
and is a caching system
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Implementation of the class"""
    def __init__(self):
        """Transfers the init from the parent class"""
        super().__init__()

    def put(self, key, item):
        """Inserts item into the cache data"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Gets items from the cache data"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
