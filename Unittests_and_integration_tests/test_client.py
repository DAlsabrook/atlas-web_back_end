#!/usr/bin/env python3
"""Testing client stuffs"""
import unittest
from parameterized import parameterized, parameterized_class
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

org_payload = {
    "login": "google",
    "id": 1342004,
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
    "url": "https://api.github.com/orgs/google",
    "repos_url": "https://api.github.com/orgs/google/repos",
    "events_url": "https://api.github.com/orgs/google/events",
    "hooks_url": "https://api.github.com/orgs/google/hooks",
    "issues_url": "https://api.github.com/orgs/google/issues",
    "members_url": "https://api.github.com/orgs/google/members{/member}",
    "public_members_url": "https://api.github.com/orgs/google/public_members{/member}",
    "avatar_url": "https://avatars.githubusercontent.com/u/1342004?v=4",
    "description": "Google"
}

repos_payload = [
    {"id": 1, "name": "repo1", "license": {"key": "apache-2.0"}},
    {"id": 2, "name": "repo2", "license": {"key": "apache-2.0"}},
    {"id": 3, "name": "repo3", "license": {"key": "mit"}},
]

expected_repos = ["repo1", "repo2", "repo3"]

apache2_repos = ["repo1", "repo2"]

@parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload, "expected_repos": expected_repos, "apache2_repos": apache2_repos, "TEST_PAYLOAD": test_payload}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): test module
    """

    @classmethod
    def setUpClass(cls):
        """set up tests

        Returns:
            _type_: mocked response
        """
        cls.get_patcher = patch('requests.get') # mock patch
        cls.mock_get = cls.get_patcher.start()
        def side_effect(url): #check the callers url
            if url == "https://api.github.com/orgs/google":
                return MockResponse(cls.org_payload)
            elif url == "https://api.github.com/orgs/google/repos":
                return MockResponse(cls.repos_payload)
            return MockResponse(None)
        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls): #simply stops the request.get
        """Tear down class method to stop the patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test GithubOrgClient.public_repos"""
        githubOrg = GithubOrgClient('google')
        self.assertEqual(githubOrg.public_repos(), self.expected_repos)

class MockResponse:
    """Used to mock request.get for other class
    """
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data


if __name__ == "__main__":
    unittest.main()
