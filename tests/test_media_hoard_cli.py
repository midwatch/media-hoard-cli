#!/usr/bin/env python
"""Tests for `media_hoard_cli` package."""
# pylint: disable=redefined-outer-name

import pytest

from click.testing import CliRunner

from media_hoard_cli import cli
from media_hoard_cli import hoard

NIDS = ['YKIKuCiQAl']
def test_new_item():

    # item = hoard.new_item('title', 'path/to/file.pdf')
    item = hoard.new('Intersting Item', 'file.pdf')

    assert item.nid == NIDS[0]
    assert item.name == "interesting_item.pdf"
    assert item.src == 'file.pdf'
    assert item.title == 'Interesting Item'


def test_cli_add():
    runner = CliRunner()
    result = runner.invoke(cli.main, ['add', 'Intesting Item', 'file.pdf'])
    assert result.exit_code == 0

    expected = """Interesting Item

  - http://localhost/YKIKuCiQAl/interesting_item.pdf

"""

    assert result.output == expected

# def test_command_line_interface():
#     """Test the CLI."""
#     runner = CliRunner()
#     result = runner.invoke(cli.main)
#     assert result.exit_code == 0
#     assert 'media_hoard_cli.cli.main' in result.output
#     help_result = runner.invoke(cli.main, ['--help'])
#     assert help_result.exit_code == 0
#     assert '--help  Show this message and exit.' in help_result.output
