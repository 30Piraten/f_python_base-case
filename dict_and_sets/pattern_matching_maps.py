media_records = {
    "name": "book",
    "api": 2,
    "authors": ["Author1", "Author2"],
    "type": "book"
}


def get_media_creators(record: dict) -> list:
    match record:
        case {"type": "book", "api": 2, "authors": [*names]}:
            return names
        case {"type": "book", "api": 1, "author": name}:
            return [name]
        case {"type": "book", "api": _, "authors": _}:
            raise ValueError(f"Invalid 'book' rekord: {record!r}")
        case {"type": "movie", "director": name}:
            return [name]
        case _:
            raise ValueError(f"Invalid rekord: {record!r}")


if __name__ == "__main__":
    result = get_media_creators(media_records)
    print(result)
