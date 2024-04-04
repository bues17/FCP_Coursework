import matplotlib.pyplot as plt
import random

class Person:
    def __init__(self, opinion,position):
        self.opinion = opinion
        self.position = position


def generate_1d_grid(number_neighbours):
    return [generate_neighbour(i) for i in range(0,number_neighbours-1)]

def generate_neighbour(pos):
    opinion = random.random()
    return Person(opinion,pos)

def apply_rule(person: Person, neighbour: Person, T, beta):
    # apply mathematical function between neighbour and person as specified in the question.
    x_i = person.opinion
    x_j = neighbour.opinion
    if x_i - x_j < T:
        person.opinion = x_i + beta * (x_j - x_i)
        neighbour.opinion = x_j + beta * (x_i - x_j)
    pass

def decide_rand_neighbour(person : Person, _grid : list):
    # if at left side of grid, choose right neighbour
    if person.position == 0:
        random_neighbour_index = 2 
    # if at right side of grid, choose left neighbour
    elif person.position == len(_grid)-1:
        random_neighbour_index = len(_grid)-2
    # else randomly choose between the left and right neighbour:
    else:
        random_neighbour_index= random.choice([person.position-1,person.position+1])
    return _grid[random_neighbour_index]

def update_grid(_grid, T, beta):
    # choose random person and for him, a random neighbour (left or right)
    random_person = random.choice(_grid)
    random_neighbour = decide_rand_neighbour(random_person,_grid)
    # apply rule to them.
    apply_rule(random_person,random_neighbour,T,beta)
    pass

def plot_timestep(timestep):
    # plot the grid at the given timestep
    pass

def main(T=0.2, beta=0.2,size=10):
    # generate grid
    grid = generate_1d_grid(size)
    for timestep in range(100):
        update_grid(grid,T,beta)
    # update grid for 100 time steps
    pass


# run main function
if __name__ == "__main__":
    main()