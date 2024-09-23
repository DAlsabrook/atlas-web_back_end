#!/usr/bin/env python3
"""Module to perform unittests"""
import unittest
from utils import access_nested_map
from parameterized import parameterized


class Test_utils(unittest.TestCase):
    """Test class

    Args:
        unittest (_type_): Test module
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Use parameterization to test nested map util"""
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
