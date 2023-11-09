# Destructuring nested tuples with match/case

# Case
frucht = [
    ("Apfel", "Grun", "Gala", (1.50, 1.75)),
    ("Banane", "Gelb", "Babybanane", (1.20, 1.25)),
    ("Erdbeere", "Rot", "Elsanta", (2.49, 2.50)),
    ("Traube", "Blau", "Red Globe", (2.99, 3.00)),
    ("Birne", "Grun", "Anjou", (1.80, 1.99)),
    ("Kirsche", "Schwarz", "Rainer", (3.50, 3.55)),
]


def nested_tuples():
    for f in frucht:
        match f:
            case [name, farbe, _, (preis_x, preis_y)] if preis_y <= 3:
                print(f"{name:10} | {farbe:7} | {
                      preis_x:3.2f} | {preis_y:3.2f}")


# The subject of this match is "f", which is each of the tuples

# Trigger
if __name__ == "__main__":
    nested_tuples()
