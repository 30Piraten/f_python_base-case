names = [
    ("gary", "x", "yara", "baldwin", "spence", "kubie")
]


for n in names:
    match n:
        case [name, _, _, *rest] if n is not None:
            print(f"{name} | {rest}")
