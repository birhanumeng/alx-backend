#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


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
        ''' Return dict of pagination data.
            Dict key/value pairs consist of the following:
              index - the start index of the page
              next_index - the start index of the next page
              page_size
              page_size - the number of items on the page
              data - the data in the page itself '''
        assert 0 <= index < len(self.dataset())
        indexed_dataset = self.indexed_dataset()
        indexed_page = {}

        idx = index
        while (len(indexed_page) < page_size and idx < len(self.dataset())):
            if idx in indexed_dataset:
                indexed_page[i] = indexed_dataset[i]
            idx += 1

        page_key = indexed_page.keys()
        page_value = list(indexed_page.values())

        return {
            'index': index,
            'next_index': max(page_key) + 1,
            'page_size': len(page_value),
            'data': page_value
        }
