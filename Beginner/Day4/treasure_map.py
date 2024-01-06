#!/usr/bin/python3

row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print("{}\n{}\n{}".format(row1, row2, row3))
position = input("Where would you want to put the treasure? ")
row = int(position[0])
column = int(position[1])
selected_row = map[column - 1]
selected_row[row - 1] = "X"
print("{}\n{}\n{}".format(row1, row2, row3))
