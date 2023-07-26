#!/usr/bin/env python3
"""Implementation of LFU cache replacement policy"""


import collections
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFU Cache class that inherits from BaseCaching."""
    def __init__(self):
        """ Initialize LFU cache. """
        super().__init__()
        self.keys = []
        self.counter = collections.Counter()

    def put(self, key, item):
        """ Put item in cache. """
        if key is not None and item is not None:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS
                    and key not in self.cache_data.keys()):
                # Discard least frequently used item, use LRU for ties
                discard = self.keys[0]
                for k in self.keys:
                    if self.counter[k] < self.counter[discard]:
                        discard = k
                self.keys.remove(discard)
                del self.cache_data[discard]
                del self.counter[discard]
                print("DISCARD: {}".format(discard))

            self.cache_data[key] = item
            if key in self.keys:
                self.keys.remove(key)
            self.keys.append(key)
            self.counter[key] += 1

    def get(self, key):
        """ Get item from cache. """
        if key is not None and key in self.cache_data.keys():
            self.keys.remove(key)
            self.keys.append(key)
            self.counter[key] += 1
            return self.cache_data.get(key)
        return None
