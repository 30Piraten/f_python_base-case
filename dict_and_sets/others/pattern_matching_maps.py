# Handling semi structured data:
# such as JSON records
from collections import OrderedDict

media_records_1 = dict(
    api=1,
    author="Thomas Wolfe",
    type="book",
    title="Look, Homeward Angel"
)

media_records_2 = OrderedDict(
    api=2,
    type="book",
    title="Irish Bard",
    authors="Torre Marthe Raut".split()
)


def get_media_creators(record: dict) -> list:
    match record:
        case {"type": "book", "api": 2, "authors": [*names]}:
            return names
        case {"type": "book", "api": 1, "author": name}:
            return [name]
        case {"type": "book", "api": _, "authors": _}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {"type": "movie", "director": name}:
            return [name]
        case _:
            raise ValueError(f"Invalid record: {record!r}")


if __name__ == "__main__":
    result = get_media_creators(media_records_1)
    result_2 = get_media_creators(media_records_2)
    print(f"{result} | {result_2}")
