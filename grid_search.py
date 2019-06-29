

def is_present(grid, search_grid):

   for i in range(len(grid)):
       for j in range(len(grid)):
        if (grid[i] == search_grid[i])

        


if __name__ == '__main__':
    
    grid = []
    search_grid = []

    rows = int(input())
    columns = int(input())

    for i in range(rows):
        col = []
        for j in range(columns):
            num = int(input())
            col.append(num)

        grid.append(col)

    print("search_grid:")

    rows = int(input())
    columns = int(input())

    for i in range(rows):
        col = []
        for j in range(columns):
            num = int(input())
            col.append(num)

        search_grid.append(col)

    print(is_present(grid, search_grid))





