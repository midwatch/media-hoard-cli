"""Main module."""

from dataclasses import asdict, dataclass, field
from pathlib import Path

import nanoid
import yaml

@dataclass
class Item:

    title: str
    pdf_end_pg: int
    doc_end_pg: int

    children: list = field(default_factory=list)
    doc_start_pg: int = field(default=1)
    pdf_start_pg: int = field(default=1)
    sub_title: str = field(default="")

    name: str = field(init=False)
    pages: tuple = field(init=False)

    def __post_init__(self):
        """Initilize dynamic members."""
        slug = self.title.lower().replace(' ', '_')

        self.name = f'{slug}.pdf'
        self.pages = tuple(range(self.pdf_start_pg, self.pdf_end_pg + 1))


def get_config(path):
    """Return config from yaml file at path."""
    with Path(path).open(encoding='utf-8') as fd_in:
        return yaml.safe_load(fd_in)


def new_item(title, src):
    """Create a new Item object.

    :param title: User friendly title for item
    :type title: str
    :param src: path to item
    :type src: str

    :return: Item
    :rtype: Item
    """
    return Item(title=title, src=src)
