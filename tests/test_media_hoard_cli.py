#!/usr/bin/env python
"""Tests for `media_hoard_cli` package."""
# pylint: disable=redefined-outer-name

from click.testing import CliRunner

from media_hoard_cli import cli, hoard

NIDS = ['YKIKuCiQAl']


def test_new_item(mocker):
    """Test create new Item object."""
    mocker.patch('media_hoard_cli.hoard.nanoid.generate', return_value=NIDS[0])
    item = hoard.new_item(title='Basic Test File',
                          src='tests/fixtures/basic_file.pdf')

    assert item.nid == NIDS[0]
    assert item.name == "basic_test_file.pdf"
    assert item.src == 'tests/fixtures/basic_file.pdf'
    assert item.title == 'Basic Test File'


def test_cli_add(mocker, tmp_path):
    """Test adding a single file."""
    mocker.patch('media_hoard_cli.hoard.nanoid.generate', return_value=NIDS[0])
    runner = CliRunner()
    result = runner.invoke(cli.main, [
        'add', '--cfg-file', 'tests/fixtures/config.yaml', '--upload-dir',
        tmp_path, 'Basic Test File', 'tests/fixtures/basic_file.pdf'
    ])

    print(result.output)
    assert result.exit_code == 0
    assert (tmp_path / NIDS[0] / 'basic_test_file.pdf').is_file()

    expected = """Basic Test File

- http://localhost/YKIKuCiQAl/basic_test_file.pdf

"""

    assert result.output == expected
