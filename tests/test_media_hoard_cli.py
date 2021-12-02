#!/usr/bin/env python
"""Tests for `media_hoard_cli` package."""
# pylint: disable=redefined-outer-name

import pytest

from click.testing import CliRunner

from media_hoard_cli import cli
from media_hoard_cli import hoard

NIDS = ['YKIKuCiQAl']


def test_new_item(mocker):
    mocker.patch('media_hoard_cli.hoard.nanoid.generate', return_value=NIDS[0])
    item = hoard.new_item(title='Interesting Item', src='file.pdf')

    assert item.nid == NIDS[0]
    assert item.name == "interesting_item.pdf"
    assert item.src == 'file.pdf'
    assert item.title == 'Interesting Item'


def test_cli_add(tmp_path):
    runner = CliRunner()
    result = runner.invoke(cli.main, ['add', '--cfg-file', 'tests/fixtures/config.yaml',
        '--upload-dir', 'tmp_path',
        'Intesting Item', 'file.pdf'])

    assert result.exit_code == 0

#     expected = """Interesting Item

#   - http://localhost/YKIKuCiQAl/interesting_item.pdf

# """

#     assert result.output == expected
