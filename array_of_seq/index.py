# Unpacking Function Calls and Sequence Literals with *

def case(x, y, z, *rest):
    return x, y, z, rest


# Further Case samples
def test():
    a, *rest, b, c = range(6)
    return (a, rest, b, c)


# Nested unpacking
stadt = [
    ("Berlin", ("Ortsnetzkennzahl", 30), "Mitte", "Humboldt-Gymnasium"),
    ("Munchen", ("Ortsnetzkennzahl", 89),
     "Alstadt-Lehel", "Gymnasium bei St. Anna"),
    ("Hamburg", ("Ortsnetzkennzahl", 40), "Hamburg-Mitte", "Gymnasium Eppendorf"),
    ("Koln", ("Ortsnetzkennzahl", 221), "Innenstadt", "Heirich-Heine-Gymnasium"),
    ("Frankfurt am Main", ("Ortsnetzkennzahl", 69),
     "Innenstadt", "Lessing-Gymnasium"),
    ("Stuttgart", ("Ortsnetzkennzahl", 711), "Stuttgart-Mitte", "Kepler-Gynmasium")
]


def main():
    print(f"{"":15} | {"area":>20} | {"district":>15} | {"code":>0}")
    for name, (area, code), district, _, in stadt:
        if code < 50:
            print(f"{name:15} | {area:20} | {district:15} | {code:3}")


# Trigger:
if __name__ == "__main__":
    main()
    #
    print()
    r = case(*[1, 3], 5, *range(8, 21))
    test()

    print(r)
