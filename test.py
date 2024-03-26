import matplotlib.pyplot as plt
import random

class Person:
    def __init__(self, opinion):
        self.opinion = opinion


def generate_1d_grid(number_neighbours):
    return [generate_neighbour() for i in range(number_neighbours)]

def generate_neighbour():
    opinion = random.random()
    return Person(opinion)

def apply_rule(person: Person, neighbour: Person, T, beta):
    # apply mathematical function between neighbour and person as specified in the question.
    x_i = person.opinion
    x_j = neighbour.opinion
    if x_i - x_j < T:
        person.opinion = x_i + beta * (x_j - x_i)
        neighbour.opinion = x_j + beta * (x_i - x_j)
    pass

def update_grid(_grid, T, beta):
    # choose random person and for him, a random neighbour (left or right)
    # apply rule to them.
    # need to check edge cases - in that case the neighbour it determines is pre-determined.
    pass

def plot_timestep(timestep):
    # plot the grid at the given timestep
    pass

def main(T=0.2, beta=0.2):
    # generate grid
    # update grid for 100 time steps
    pass


# run main function
if __name__ == "__main__":
    main()