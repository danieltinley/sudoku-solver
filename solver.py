# Written by Daniel Tinley in 2020

grid1 = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

grid2 = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0]]

grid3 = [[8, 0, 0, 0, 5, 6, 0, 9, 7],
         [0, 0, 0, 0, 0, 0, 2, 0, 5],
         [0, 0, 4, 0, 0, 0, 3, 0, 0],
         [0, 0, 1, 0, 0, 2, 0, 4, 0],
         [0, 7, 0, 0, 0, 0, 0, 0, 0],
         [6, 0, 5, 3, 0, 4, 0, 0, 1],
         [0, 4, 0, 0, 0, 0, 0, 6, 0],
         [7, 1, 0, 0, 8, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 3, 0, 0, 0]]

# Moves along the list, replacing every '0' and backtracking where necessary until it reaches the end of the list
def solve(grid):
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if valid(grid, y, x, n):
                        grid[y][x] = n
                        solve(grid)
                        grid[y][x] = 0
                return

    print("\nSolution:")
    print_grid(grid)

# Checks if a specific number can go in a specific spot
def valid(grid, y, x, n):
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
    for i in range(0, 9):
        if grid[i][x] == n:
            return False

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == n:
                return False

    return True

# Allows the user to enter a custom Sudoku puzzle
def create_grid():
    print("\nPlease enter each row of your Sudoku puzzle individually, with each number separated by a space.")

    row1 = [int(x) for x in input("Row 1: ").split()]
    row2 = [int(x) for x in input("Row 2: ").split()]
    row3 = [int(x) for x in input("Row 3: ").split()]
    row4 = [int(x) for x in input("Row 4: ").split()]
    row5 = [int(x) for x in input("Row 5: ").split()]
    row6 = [int(x) for x in input("Row 6: ").split()]
    row7 = [int(x) for x in input("Row 7: ").split()]
    row8 = [int(x) for x in input("Row 8: ").split()]
    row9 = [int(x) for x in input("Row 9: ").split()]
    new_grid = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

    print("\nPuzzle:")
    print_grid(new_grid)
    solve(new_grid)

# Displays the stored puzzle list in a more readable format
def print_grid(grid):
    gridrow0 = [i.replace('0', ' ') for i in (' '.join(map(str, grid[0])).split())]
    gridrow1 = [i.replace('0', ' ') for i in (' '.join(map(str, grid[1])).split())]
    gridrow2 = [i.replace('0', ' ') for i in (' '.join(map(str, grid[2])).split())]
    gridrow3 = [i.replace('0', ' ') for i in (' '.join(map(str, grid[3])).split())]
    gridrow4 = [i.replace('0', ' ') for i in (' '.join(map(str, grid[4])).split())]
    gridrow5 = [i.replace('0', ' ') for i in (' '.join(map(str, grid[5])).split())]
    gridrow6 = [i.replace('0', ' ') for i in (' '.join(map(str, grid[6])).split())]
    gridrow7 = [i.replace('0', ' ') for i in (' '.join(map(str, grid[7])).split())]
    gridrow8 = [i.replace('0', ' ') for i in (' '.join(map(str, grid[8])).split())]

    print('', gridrow0[0], gridrow0[1], gridrow0[2], '|', gridrow0[3], gridrow0[4], gridrow0[5], '|', gridrow0[6],
          gridrow0[7], gridrow0[8], '\n',
          gridrow1[0], gridrow1[1], gridrow1[2], '|', gridrow1[3], gridrow1[4], gridrow1[5], '|', gridrow1[6],
          gridrow1[7], gridrow1[8], '\n',
          gridrow2[0], gridrow2[1], gridrow2[2], '|', gridrow2[3], gridrow2[4], gridrow2[5], '|', gridrow2[6],
          gridrow2[7], gridrow2[8], '\n', '------+-------+------\n',
          gridrow3[0], gridrow3[1], gridrow3[2], '|', gridrow3[3], gridrow3[4], gridrow3[5], '|', gridrow3[6],
          gridrow3[7], gridrow3[8], '\n',
          gridrow4[0], gridrow4[1], gridrow4[2], '|', gridrow4[3], gridrow4[4], gridrow4[5], '|', gridrow4[6],
          gridrow4[7], gridrow4[8], '\n',
          gridrow5[0], gridrow5[1], gridrow5[2], '|', gridrow5[3], gridrow5[4], gridrow5[5], '|', gridrow5[6],
          gridrow5[7], gridrow5[8], '\n', '------+-------+------\n',
          gridrow6[0], gridrow6[1], gridrow6[2], '|', gridrow6[3], gridrow6[4], gridrow6[5], '|', gridrow6[6],
          gridrow6[7], gridrow6[8], '\n',
          gridrow7[0], gridrow7[1], gridrow7[2], '|', gridrow7[3], gridrow7[4], gridrow7[5], '|', gridrow7[6],
          gridrow7[7], gridrow7[8], '\n',
          gridrow8[0], gridrow8[1], gridrow8[2], '|', gridrow8[3], gridrow8[4], gridrow8[5], '|', gridrow8[6],
          gridrow8[7], gridrow8[8])

# Main menu
def main():
    x = input("\nWhich puzzle would you like to solve? Choose either a preset one (1, 2, or 3), or you can enter 'custom' to solve your own.\n> ")

    if x == '1':
        print("\nPuzzle:")
        print_grid(grid1)
        solve(grid1)
        main()
    elif x == '2':
        print("\nPuzzle:")
        print_grid(grid2)
        solve(grid2)
        main()
    elif x == '3':
        print("\nPuzzle:")
        print_grid(grid3)
        solve(grid3)
        main()
    elif x == 'custom':
        create_grid()
        main()
    else:
        print("\nERROR: Please pick an existing puzzle.")
        main()


main()