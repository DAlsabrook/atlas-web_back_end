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
        mockOrg.return_value = {'repos_url':
                                'https://api.github.com/orgs/google/repos'}
        githubOrg = GithubOrgClient('google')
        result = githubOrg._public_repos_url
        self.assertEqual('https://api.github.com/orgs/google/repos', result)

    @patch('client.get_json',
           return_value=[{'name': 'repo1'}, {'name': 'repo2'}])
    def test_public_repos(self, mock_get_json):
        """Testing GithubOrgClient.public_repos"""
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mockRepos:
            mockRepos.return_value = "https://api.github.com/orgs/google/repos"
            githubOrg = GithubOrgClient('google')
            result = githubOrg.public_repos()
            self.assertEqual(result, ['repo1', 'repo2'])
            mockRepos.assert_called_once()
            mock_get_json.assert_called_once_with(
                'https://api.github.com/orgs/google/repos'
                )

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Testing GithubOrgClient.has_license"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
