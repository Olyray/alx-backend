#!/usr/bin/env python3
"""
A module to implement a function that returns the range of indexes
for pagination parameters
"""

import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function that returns the raneg of index"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """The get page method"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0
        # Use index range to paginate the dataset
        correct_index = index_range(page, page_size)
        # Call the dataset method to get the list of the dataset
        list_of_dataset = self.dataset()
        # Return an empty list if the range is more than length of the dataset
        if correct_index[1] > len(list_of_dataset):
            return []
        else:
            return list_of_dataset[correct_index[0]: correct_index[1]]
