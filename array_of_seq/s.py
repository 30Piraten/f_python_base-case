# Test Case

names = [
    "gary", "x", "yara", "baldwin", "spence", "kubie"
]

r = names[:2]
r1 = names[2:]
r2 = names[:3]
r3 = names[3:]

print(r)
print(r1)
print(r2)
print(r3)

print()

# Slice Objects: 1
s = names[::3]
s1 = names[::-1]
s2 = names[::-2]

print(s)
print(s1)
print(s2)
print()

# Slice Objects: 2
buch = """
    0.........8.....16.............30.......42.....
    198       12     ebook          en       $19.95
    208       5      paperback      br       $12.75
    012       10     ebook          fr       $22.45
    895       9      ebook          en       $45.95
    892       2      paperback      it       $28.00
    """

# We can name our slices, instead of hardcoding it:
# defined named slices for the columns
SERIAL_NUMBER = slice(0, 8)
QUANTITY = slice(8, 16)
FORMAT = slice(16, 30)
LANGUAGE = slice(30, 42)
PRICE = slice(42, None)

# split the input into lines
buch_items = buch.split("\n")[2:]

# Iterate through the items
for b in buch_items:
    # Trigger:
    print(b[SERIAL_NUMBER], b[QUANTITY], b[PRICE], b[LANGUAGE])
