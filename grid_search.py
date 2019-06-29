
def helper_function(grid, search_grid):

    col = len(search_grid)
    rows = len(search_grid[0])

    check = is_present(grid[rows][col],search_grid)
    return check


def is_present(grid, search_grid):

   for i in range(len(grid)):
       for j in range(len(grid[i])):
        if (grid[i][j] == search_grid[i][j]):
            if(grid[i][j+1] == search_grid[i][j+1]):
                if (grid[i+1][j] == search_grid[i+1][j]):
                    if(grid[i+1][j+1] == search_grid[i+1][j+1]):
                        return True
        return False


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





