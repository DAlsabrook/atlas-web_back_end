#!/usr/bin/env python3
"""Testing client stuffs"""
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Testing GithubOrgClient class"""

    @parameterized.expand([
        ('google', {'login': 'orgName'}),
        ('abc', {'login': 'orgName'})
    ])
    @patch('client.get_json', return_value={'login': 'orgName'})
    def test_org(self, org, expected, getJson):
        """Test GithubOrgClient.org"""
        githubOrg = GithubOrgClient(org)
        result = githubOrg.org
        getJson.assert_called_once_with(f'https://api.github.com/orgs/{org}')
        self.assertEqual(result, expected)

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mockOrg):
        """Testing githubOrgClient._public_repos_url"""
        mockOrg.return_value = {'repos_url': 'https://api.github.com/orgs/google/repos'}
        githubOrg = GithubOrgClient('google')
        result = githubOrg._public_repos_url
        self.assertEqual('https://api.github.com/orgs/google/repos', result)


if __name__ == "__main__":
    unittest.main()
