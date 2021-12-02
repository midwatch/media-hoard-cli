"""Console script for Media Hoard CLI."""

import sys

import click

from media_hoard_cli import hoard


@click.group()
def main():
    """Empty click anchor function."""

@click.command()
@click.option('--cfg-file', default="$HOME/.config/media_hoard/config.yaml",
    help="path to config file")
@click.option('--upload-dir', help="overide cfg upload-dir")
@click.argument('title')
@click.argument('src')
def add(cfg_file, upload_dir, title, src):
    """Add a new file from local host.

    TITLE: User friendly title
    SRC: path to item to add (path/to/file.pdf)
    """
    # media_hoard add --chunk chunks.csv TITLE path/to/file.pdf

    # print(title)        # Intersting item
    # print(cfg_file)     # $HOME/.config/media_hoard/config.yaml
    # print(src)          # file.pdf

    # cfg.upload_dir = "justin@marauder/volume1/web/stacks"
    # ctx.run(f'rsync -r work_dir config.upload_dir')

    # with tempdir as work_dir:
    #     cp(item['src'], "work_dir/item['nid']/item['name']")
    #     rsync('work_dir', "cfg.upload_dir/item['nid']")
    #     # justin@marauder/volume1/web/stacks/{nid}/item_name.pdf

    # print(f'{item.title}')
    # print()
    # print(f'- {cfg.item_url}')

    # with tempfile.TemporaryDirectory() as tmpdirname:
    #     print(tmpdirname)

    #     /tmp/tmpzqkae43n


    try:
        cfg = hoard.get_config(cfg_file)
        cfg['upload_dir'] = cfg['upload_dir'] if not upload_dir else upload_dir

    except FileNotFoundError:
        raise click.ClickException(f'Config file not found at {cfg_file}')

    return 0


main.add_command(add)

if __name__ == "__main__":
    sys.exit(main())  # pylint: disable=no-value-for-parameter
