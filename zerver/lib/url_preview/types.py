from dataclasses import dataclass
from typing import Literal, Optional


@dataclass
class UrlEmbedData:
    type: Optional[str] = None
    html: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None

    def merge(self, other: "UrlEmbedData") -> None:
        if self.title is None and other.title is not None:
            self.title = other.title
        if self.description is None and other.description is not None:
            self.description = other.description
        if self.image is None and other.image is not None:
            self.image = other.image

    def merge_dict(self, other: dict) -> None:
        if self.title is None and other.get('title') is not None:
            self.title = other['title']
        if self.description is None and other.get('description') is not None:
            self.description = other['description']
        if self.image is None and other.get('image') is not None:
            self.image = other['image']

    def is_complete(self) -> bool:
        return (self.title is not None and
                self.description is not None and
                self.image is not None)

@dataclass
class UrlOEmbedData(UrlEmbedData):
    type: Literal["photo", "video"]
    html: Optional[str] = None
