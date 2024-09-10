#!/usr/bin/env python3
"""
Module for a function pagination set up for pagination
"""
import csv
import math
from typing import List


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the class
        """
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
        """Method to get a specific page from the dataset
        """
        assert isinstance(page, int) and isinstance(page_size, int), """
        raised when page and/or page_size are not ints
        """
        assert page > 0 and page_size > 0, "raised with negative values"
        start_index, end_index = self.index_range(page, page_size)
        dataset = self.dataset()
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

    @staticmethod
    def index_range(page, page_size):
        """function to get index of pagination range
        """
        return (page_size * (page - 1) if page > 1 else 0, page_size * page)

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """Creates a dict of information of pagination
        """
        dataset = self.dataset()
        total_items = len(dataset)
        total_pages = math.ceil(total_items / page_size)
        data = self.get_page(page, page_size)
        pageInfor = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages,
        }
        return pageInfor


server = Server()

print(server.get_hyper(1, 2))
print("---")
print(server.get_hyper(2, 2))
print("---")
print(server.get_hyper(100, 3))
print("---")
print(server.get_hyper(3000, 100))
