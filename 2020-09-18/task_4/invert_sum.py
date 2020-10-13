import random


# maximum number of iteration
# set it to None to deactivate this feature
MAX_ITER = 10000
# MAX_ITER = None


def invert_sum():

    # select random number
    while True:

        number = random.randrange(0, 1000)

        # check exceptions
        if number not in (196, 879):
            break

    # number of additions
    print(f"Number generated = {number},", end=" ")
    count = 0

    while True:

        # invert the number
        inverse = str(number)
        inverse = int(inverse[::-1])

        # exit condition
        if inverse == number:
            print(f"Final addition = {number}")
            return count

        count += 1
        number = number + inverse

        # preventing infinite loop
        if MAX_ITER is not None:
            if count == MAX_ITER:
                print(f"Number of iterations exceeded MAX_ITER={MAX_ITER}")
                return count


if __name__ == "__main__":

    values = []

    # run the 100 rounds
    for i in range(100):
        print(f"round {i+1},", end=" ")
        count = invert_sum()
        values.append(count)

    # compute the average
    average = sum(values) / len(values)
    print(f"The average = {average}")
