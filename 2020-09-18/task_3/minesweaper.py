import random


def minesweeper(size, num_bombs):

    # create a size x size board of enpty spaces
    table = [["." for i in range(size)] for j in range(size)]

    # place the bombs
    coordinates = [(i, j) for i in range(size) for j in range(size)]

    bombs = random.sample(coordinates, num_bombs)

    for x, y in bombs:
        table[x][y] = "X"

    return table


if __name__ == "__main__":

    # test
    size = int(input("Enter size of the board: "))
    num_bombs = int(input("Enter number of bombs: "))

    if num_bombs > size ** 2:
        print("Impossible")

    else:
        table = minesweeper(size, num_bombs)

        for line in table:
            print(' '.join(line))
