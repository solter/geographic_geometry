#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `geographic_geometry` package."""


import unittest
from click.testing import CliRunner

from geographic_geometry import geographic_geometry
from geographic_geometry import cli


class TestGeographic_geometry(unittest.TestCase):
    """Tests for `geographic_geometry` package."""

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
        assert 'geographic_geometry.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
