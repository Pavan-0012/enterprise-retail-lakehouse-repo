from dataclasses import dataclass


@dataclass
class StorageObject:

    name: str

    size: int

    bucket: str

    last_modified: str