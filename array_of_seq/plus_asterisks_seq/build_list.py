# A list with 3 lists of lenght 3
# using a list comprehension
board = [["_"] * 3 for _ in range(3)]
# board = [["_"] * 3 for i in range(3)]
print(board)
board[1][2] = "Y"
print(board)

print()
# Using a for loop
board_y = []
for _ in range(3):
    row = ["_"] * 3
    board_y.append(row)
print(board_y)
board_y[1][2] = "Y"
print(board_y)

print()

# A different way of this: not advised!
board_2 = [["_"] * 3] * 3
print(board_2)

board_2[1][2] = "0"
# you can see from here that all rows are marked
# unlike the list comprehension used earlier.
print(board_2)

print()
# Using a for loop
row = ["_"] * 3
board_x = []

# With the for loop, the same row is
# appended 3 times to the board_2.
for _ in range(3):
    board_x.append(row)

print(board_x)
board_x[1][2] = "0"
print(board_x)
