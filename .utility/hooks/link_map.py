from dataclasses import dataclass
from pathlib import Path


@dataclass
class LinkData:
    source: Path
    target: Path

    def to_json(self) -> dict:
        """Convert LinkData to JSON-serializable dictionary."""
        return {"Path": str(self.source), "Target": str(self.target)}

    @classmethod
    def from_json(cls, data: dict) -> "LinkData":
        """Create LinkData from JSON dictionary."""
        return cls(source=Path(data["Path"]), target=Path(data["Target"]))


class LinkMap:
    def __init__(self, link_data=None):
        if link_data:
            self._link_data = link_data
        else:
            self._link_data: list[LinkData] = []

    def add_link(self, link: LinkData) -> None:
        """Add a LinkData element to the link_data list.

        Args:
            link: LinkData object to add
        """
        self._link_data.append(link)

    @property
    def links(self):
        return self._link_data

    def to_json(self) -> list[dict]:
        """Convert LinkMap to JSON-serializable list of dictionaries."""
        return [link.to_json() for link in self._link_data]

    @classmethod
    def from_json(cls, data: list[dict]) -> "LinkMap":
        """Create LinkMap from JSON list of dictionaries."""
        return cls([LinkData.from_json(item) for item in data])
