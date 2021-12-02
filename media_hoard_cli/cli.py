"""Console script for Media Hoard CLI."""

import sys

import click


@click.group()
def main():
    """Empty click anchor function."""

@click.command()
@click.option('--cfg-file', default="$HOME/.config/media_hoard/config.yaml",
    help="path to config file")
@click.argument('title')
@click.argument('src')
def add(cfg_file, title, src):
    """Add a new file from local host.

    TITLE: User friendly title
    SRC: path to item to add (path/to/file.pdf)
    """
    # media_hoard add --chunk chunks.csv TITLE path/to/file.pdf

    # print(title)        # Intersting item
    # print(cfg_file)     # $HOME/.config/media_hoard/config.yaml
    # print(src)          # file.pdf


    # config file at $HOME/.config/media_hoard/config.{???}

    # cfg.item_url = "http://stacks/{item.nid}/{item.name}"            # user supplied so we have to use
                                                                # string template
    # cfg.upload_dir = "justin@marauder/volume1/web/stacks"
    # ctx.run(f'rsync -r work_dir config.upload_dir')

    # cfg = hoard.load_config()
    # item = hoard.new_item('title', 'path/to/file.pdf')

    # item['nid']       # nano_id
    # item['name']      # {title_slug}.{ext}
    # item['src']       # path/to/file
    # item['title']

    # with tempdir as work_dir:
    #     cp(item['src'], "work_dir/item['nid']/item['name']")
    #     rsync('work_dir', "cfg.upload_dir/item['nid']")
    #     # justin@marauder/volume1/web/stacks/{nid}/item_name.pdf

    # print(f'{item.title}')
    # print()
    # print(f'- {cfg.item_url}')


main.add_command(add)

if __name__ == "__main__":
    sys.exit(main())  # pylint: disable=no-value-for-parameter
