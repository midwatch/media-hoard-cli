"""Console script for Media Hoard CLI."""

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from string import Template

import click

from media_hoard_cli import hoard


@click.group()
def main():
    """Empty click anchor function."""


@click.command()
@click.option('--cfg-file',
              default="$HOME/.config/media_hoard/config.yaml",
              help="path to config file")
@click.option('--upload-dir', help="overide cfg upload-dir")
@click.argument('title')
@click.argument('src_file')
def add(cfg_file, upload_dir, title, src_file):
    """Add a new file from local host.

    TITLE: User friendly title
    SRC_FILE: path to item to add (path/to/file.pdf)
    """
    # media_hoard add --chunk chunks.csv TITLE path/to/file.pdf

    with tempfile.TemporaryDirectory() as tmpdir_name:
        try:
            cfg = hoard.get_config(cfg_file)
            cfg['upload_dir'] = cfg[
                'upload_dir'] if not upload_dir else upload_dir

            item = hoard.new_item(title, src_file)

            src_dir = Path(tmpdir_name) / item.nid
            src_dir.mkdir()
            shutil.copy(item.src, src_dir / item.name)

            subprocess.run(['rsync', '-r', src_dir, upload_dir + '/'],
                           check=True)

            item_url = Template(cfg['item_url']).substitute(item.asdict())
            print(f'{item.title}')
            print()
            print(f'- {item_url}')
            print()

        except FileNotFoundError:
            raise click.ClickException(f'Config file not found at {cfg_file}')  # pylint: disable=raise-missing-from

    return 0


main.add_command(add)

if __name__ == "__main__":
    sys.exit(main())  # pylint: disable=no-value-for-parameter
