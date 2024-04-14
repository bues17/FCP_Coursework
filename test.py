import matplotlib.pyplot as plt
import random
import numpy as np
class Person:
    def __init__(self, opinion,position):
        self.opinion = opinion
        self.position = position


def generate_1d_grid(number_neighbours):
    '''
    Input : The number of neighbours in the grids - otherwise known as the size of the 1D grid.
    Returns : A grid of Person objects, each with a random 'opinion', of size specified by the input.
    '''
    return [generate_neighbour(i) for i in range(0,number_neighbours-1)]

def generate_neighbour(pos):
    '''
    Inputs : The position at which a Person is to be generated / created.
    Returns : A Person object with the given position and a random opinion.
    '''
    opinion = random.random()
    return Person(opinion,pos)

def apply_rule(person: Person, neighbour: Person, T, beta):
    '''
    Inputs : 
        Person : Person object
        Neighbour : Person object
        Threshold : The Threshold parameter
            Increasing this will decrease the range of opinions within a 'group of people'
        beta : The coupling parameter.
          Increasing this will increase the likeliehood of there being more 'groups of people' with a similar opinion
    This procedure applies the mathematical function between the two 'people' as specified in the assignment
    '''
    # apply mathematical function between neighbour and person as specified in the question.
    x_i = person.opinion
    x_j = neighbour.opinion
    if abs(x_i - x_j) < T: # abs takes the magnitude of what is passed in.
        person.opinion = x_i + beta * (x_j - x_i)
        neighbour.opinion = x_j + beta * (x_i - x_j)
    pass

def decide_rand_neighbour(person : Person, _grid : list):
    '''
    Inputs :
        person : Person object
        _grid : A 1d list of person objects.
    Returns : A person object that is directly next to the previously passed in person object, chosen at random.
    '''
    # if at beginning ( left side ) of grid, choose right neighbour
    if person.position == 0:
        random_neighbour_index = 2
    # if at end ( right side ) of grid, choose left neighbour
    elif person.position == len(_grid)-1:
        random_neighbour_index = len(_grid)-2
    # else randomly choose between the left and right neighbour:
    else:
        random_neighbour_index= random.choice([person.position-1,person.position+1])
    return _grid[random_neighbour_index]

def update_grid(_grid, T, beta):
    '''
    Inputs:
        _grid : A 1d list of person objects.
        Threshold : Stores the value for the Threshold value specified in the assignment.
        beta : Stores the value for the 'coupling parameter'.
    '''
    # choose random person and for them, a random neighbour (left or right)
    random_person = random.choice(_grid)
    random_neighbour = decide_rand_neighbour(random_person,_grid)
    # apply rule to them.
    apply_rule(random_person,random_neighbour,T,beta)
    return _grid


def get_scatter_values(float_list: list):
    '''
    Input :
        float_list : A 2d list of lists of floats.
    Returns : 
        x_values : 1d list of x-coordinates.
        y_values : 1d list of the corresponding y-coordinates.
    
    Each float value in a given 1d list must go at x = n on the graph , where n is the index for that list ( within the 2d list ).
    The y coordinates will be the float value itself.
    '''
    y_values = []
    x_values = []

    for x in range(0,len(float_list)-1):
        x_values.append([x] * (len(float_list[x])))
        for y in float_list[x]:
            y_values.append(y)
    return x_values,y_values

def plot_hist(ax, grid):
    '''
    Inputs :
        ax : a matplotlib.pyplot.Axes object, which denotes where the graph will go on the larger figure.
        grid : 1d list of Person objects.
    '''
    final_opinions = [grid[i].opinion for i in range(0,len(grid)-1)]
    ax.hist(final_opinions)
    ax.set_xlim([0, 1])
    ax.set_xlabel("Opinion")


def plot_scatter(ax, opinon_list):
    '''
    Inputs :
        ax : a matplotlib.pyplot.Axes object, which denotes where the graph will go on the larger figure.
        opinion_list : 2d list containing the opinion values of each person, for each timestep.
    '''
    timestep_values, opinion_values = get_scatter_values(opinon_list)
    ax.scatter(timestep_values,opinion_values, color ="red",s=20) 
    ax.set_ylim([0,1])
    ax.set_ylabel("Opinion")
    ax.set_xlabel("Timestep")

def main(T=0.2, coupling=0.2,size=20):
    # generate grid
    grid = generate_1d_grid(size)
    opinions_list = [[grid[i].opinion for i in range(0, len(grid) - 1)]]
    for timestep in range(100):
        for n in range(len(grid)-1):
            grid = update_grid(grid,T,coupling)
        opinions_list.append([grid[i].opinion for i in range(0,len(grid)-1)])
        # 2d list of floats, each nthlist contains the opinions for timestep n.
    # update grid for 100 time steps
        
    fig, axs = plt.subplots(1,2)
    plot_hist(axs[0],grid)
    plot_scatter(axs[1],opinions_list)
    fig_title = str("Coupling : " + str(coupling) + ", Threshold : " + str(T))
    fig.suptitle(fig_title)
    plt.show()


# run main function
if __name__ == "__main__":
    main(0.5,0.5,100)