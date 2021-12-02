from dataclasses import dataclass, field
from pathlib import Path
import nanoid


@dataclass
class Item:
    """Class for representing a new item."""

    title: str
    src: str
    name: str = field(init=False)
    nid: str = field(init=False)

    def __post_init__(self):
        slug = self.title.lower().replace(' ', '_')
        ext = Path(self.src).suffix
        self.name = f'{slug}{ext}'
        self.nid = nanoid.generate(size=10)


def new_item(title, src):
    return Item(title=title, src=src)
