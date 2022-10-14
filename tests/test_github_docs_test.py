#!/usr/bin/env python

"""Tests for `github_docs_test` package."""


import unittest
from click.testing import CliRunner

from github_docs_test import github_docs_test
from github_docs_test import cli


class TestGithub_docs_test(unittest.TestCase):
    """Tests for `github_docs_test` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'github_docs_test.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
