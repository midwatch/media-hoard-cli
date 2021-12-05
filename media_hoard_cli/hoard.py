"""Main module."""

from dataclasses import asdict, dataclass, field
from pathlib import Path
import shutil
from string import Template

import nanoid
import yaml
from PyPDF4 import PdfFileWriter, PdfFileReader

ITEM_TEMPLATE = """$title
$sub_title

- $item_url
"""

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

    def as_dict(self):
        return asdict(self)


def _add_pdf(src, dir_stage, title):

    with Path(src).open('rb') as fd_in:
        reader = PdfFileReader(fd_in)

        end_page = reader.numPages

    item = Item(title=title, doc_end_pg=end_page, pdf_end_pg=end_page)

    shutil.copy(src, (Path(dir_stage) / item.name))

    return item


def get_id():
    return nanoid.generate(size=10)


def new_item(src, dir_stage, title):
    """Create a new Item object.

    :param src: path to file to add
    :type src: str
    :param dir_stage: path to staging directory
    :dir_stage: str
    :param title: User friendly title for item
    :type title: str

    :return: Item
    :rtype: Item
    """
    return _add_pdf(src, dir_stage, title)


def parse_config_file(path, upload_dir):
    """Return config from yaml file at path."""
    with Path(path).open(encoding='utf-8') as fd_in:
        cfg = yaml.safe_load(fd_in)
        cfg['upload_dir'] = cfg['upload_dir'] if not upload_dir else upload_dir

        if cfg['upload_dir'][-1] != '/':
            cfg['upload_dir'] = cfg['upload_dir'] + '/'

        return cfg


def render_item(item, item_id, item_url_str):

    fields = item.as_dict()
    fields['item_url'] = Template(item_url_str).substitute(nid=item_id, name=item.name)

    out = Template(ITEM_TEMPLATE).substitute(**fields)

    return out
