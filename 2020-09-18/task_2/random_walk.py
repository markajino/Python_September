import random

# some of the rounds were divergent, so i implemented a
# maximum iteration (10.000 iterations) limit for each round.
# set it to None to deactivate this feature
MAX_ITER = 10000
#MAX_ITER = None


def random_walk():

    position = [0, 0]
    num_steps = 0

    # infinite loop
    while True:

        number = random.randint(1, 4)
        num_steps += 1

        if number == 1:
            position[1] += 1

        elif number == 2:
            position[1] += -1

        elif number == 3:
            position[0] += 1

        elif number == 4:
            position[0] += -1

        # exit condition
        if position == [0, 0]:
            return num_steps

        # max iteration to reduce execution time
        if MAX_ITER is not  None:
            if num_steps == MAX_ITER:
                return num_steps


def main():

    # array to save the num_steps
    array = []

    # run 100 rounds
    for i in range(100):
        print(f"round {i+1}...", end="\r")

        num_steps = random_walk()
        array.append(num_steps)

    # compute the average
    average = sum(array) / len(array)

    return average


if __name__ == "__main__":

    average = main()
    print(f"\nAverage number of steps taken = {average}")
