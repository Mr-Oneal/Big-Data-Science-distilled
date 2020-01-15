from calculate_hypothesis import *

def compute_cost(X, y, theta):
    """
        :param X            : 2D array of our dataset
        :param y            : 1D array of the groundtruth labels of the dataset
        :param theta        : 1D array of the trainable parameters
    """

    # initialize cost
    J = 0.0
    # get number of training examples
    m = y.shape[0]
    # print("M : ", m) #97

    for i in range(m):
        hypothesis = calculate_hypothesis(X, theta, i)
        output = y[i]
        squared_error = (hypothesis - output) ** 2
        J = J + squared_error # J = 0 + 309.478464 WHEN i = 0
    J = J/(2*m)
    # print("cost", J)

    return J
