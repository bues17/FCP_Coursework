import matplotlib.pyplot as plt
import random
import numpy as np
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
    return _grid


def get_scatter_values(float_list: list):
    y_values = []
    x_values = []

    for x in range(0,len(float_list)-1):
        x_values.append([x] * (len(float_list[x])))
        for y in float_list[x]:
            y_values.append(y)
    return x_values,y_values

def plot_hist(ax, grid):
    final_opinions = [grid[i].opinion for i in range(0,len(grid)-1)]
    ax.hist(final_opinions)
    ax.set_xlim([0, 1])
    ax.set_xlabel("Opinion")


def plot_scatter(ax, opinon_list):
    timestep_values, opinion_values = get_scatter_values(opinon_list)
    ax.scatter(timestep_values,opinion_values, color ="red",s=20) 
    ax.set_ylim([0,1])
    ax.set_ylabel("Opinion")
    ax.set_xlabel("Timestep")

def main(T=0.2, beta=0.2,size=20):
    # generate grid
    grid = generate_1d_grid(size)
    opinions_list = [[grid[i].opinion for i in range(0, len(grid) - 1)]]
    for timestep in range(100):
        for n in range(len(grid)-1):
            grid = update_grid(grid,T,beta)
        opinions_list.append([grid[i].opinion for i in range(0,len(grid)-1)])
        # 2d list of floats, each nthlist contains the opinions for timestep n.
    # update grid for 100 time steps
        
    fig, axs = plt.subplots(1,2)
    plot_hist(axs[0],grid)
    plot_scatter(axs[1],opinions_list)
    fig_title = str("Coupling : " + str(beta) + ", Threshold : " + str(T))
    fig.suptitle(fig_title)
    plt.show()


# run main function
if __name__ == "__main__":
    main(0.5,0.5,100)