#!/usr/bin/env python3
"""Testing client stuffs"""
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """Testing GithubOrgClient class"""

    @parameterized.expand([
        ('google', {'login': 'orgName'}),
        ('abc', {'login': 'orgName'})
    ])
    @patch('client.get_json', return_value={'login': 'orgName'})
    def test_org(self, org, expected, getJson):
        """Test that GithubOrgClient.org returns the correct value"""
        githubOrg = GithubOrgClient(org)
        result = githubOrg.org
        getJson.assert_called_once_with(f'https://api.github.com/orgs/{org}')
        self.assertEqual(result, expected)

    @patch('client.GithubOrgClient.org', return_value={'https://api.github.com/orgs/google'})
    def test_public_repos_url(self):
        """Testing githubOrgClient._public_repos_url"""
        githubOrg = GithubOrgClient('google')
        mockedResult = githubOrg.org()
        result = githubOrg._public_repos_url()
        self.asserEqual(mockedResult, result)


if __name__ == "__main__":
    unittest.main()
