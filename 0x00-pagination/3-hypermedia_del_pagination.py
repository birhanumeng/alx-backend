#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ Takes two integer arguments: index with a None default value and
            page_size with default value of 10.
            It return a dictionary with the following key-value pairs:
                - index:  the current start index of the return page.
                - next_index: the next index to query with.
                - page_size: the current page size.
                - data: the actual page of the dataset.
        """
        assert 0 <= index < len(self.dataset())
        indexed_dataset = self.indexed_dataset()
        indexed_page = {}

        idx = index
        while (len(indexed_page) < page_size and idx < len(self.dataset())):
            if idx in indexed_dataset:
                indexed_page[idx] = indexed_dataset[idx]
            idx += 1

        page_key = indexed_page.keys()
        page_value = list(indexed_page.values())
        return {
            'index': index,
            'next_index': max(page_key) + 1,
            'page_size': len(page_value),
            'data': page_value
        }
