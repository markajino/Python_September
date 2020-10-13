import random


def main():

    table = []

    # create the 10x10 table of random S and O
    for i in range(10):

        table.append([])

        for j in range(10):

            if random.random() > .5:
                table[i].append("S")
            else:
                table[i].append("O")

    # display the table
    for line in table:
        print(" ".join(line))

    # search for the SOS pattern
    counter_d, counter_v, counter_h = 0, 0, 0

    # search through the rows
    for i in range(10):
        for j in range(8):

            word = "".join(table[i][j: j+3])

            # increment the counter
            if word == "SOS":
                counter_h += 1

    # search through the columns
    for i in range(8):
        for j in range(10):

            letters = (table[i][j], table[i+1][j], table[i+2][j])
            word = "".join(letters)

            # increment the counter
            if word == "SOS":
                counter_v += 1

    # search through the diagonals
    for j in range(8):
        diag = [table[n][j+n] for n in range(10-j)]

        for k in range(10-j-2):

            word = "".join(diag[k: k+3])
            if word == "SOS":
                counter_d += 1

    for i in range(1, 8):
        diag = [table[i+n][n] for n in range(10-i)]

        for k in range(10-i-2):

            word = "".join(diag[k: k+3])
            if word == "SOS":
                counter_d += 1

    return counter_h, counter_v, counter_d


if __name__ == "__main__":

    # test
    h, v, d = main()
    print(f"\nNumer of SOS horizontal patterns = {h}")
    print(f"Numer of SOS vertical patterns = {v}")
    print(f"Numer of SOS diagonal patterns = {d}")
