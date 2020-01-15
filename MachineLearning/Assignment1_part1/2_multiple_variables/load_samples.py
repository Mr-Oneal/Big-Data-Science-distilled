import numpy as np

def load_samples():
    # loads the data for excercise 2

    # read our data from a text file
    data = np.loadtxt("new_samples.txt", comments="#", delimiter=",", unpack=False)

    # load the first two columns into X
    X = data[:, :2]

    return X
