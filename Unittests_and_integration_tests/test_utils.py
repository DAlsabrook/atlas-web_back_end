#!/usr/bin/env python3
"""Module to perform unittests"""
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
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

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json with various inputs"""
        with patch('utils.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Test memoization

    Args:
        unittest (_type_): unittest module
    """

    def test_memoize(self):
        """Test the memoize wrapper function
        """
        class TestClass:
            """Test class"""

            def a_method(self):
                """Method to test calling"""
                return 42

            @memoize
            def a_property(self):
                """Method to wrap with memoize"""
                return self.a_method()

        testClassInstance = TestClass()

        with patch.object(testClassInstance,
                          'a_method',
                          return_value=42) as mock_a_method:
            self.assertEqual(testClassInstance.a_property, 42)
            self.assertEqual(testClassInstance.a_property, 42)
            mock_a_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
