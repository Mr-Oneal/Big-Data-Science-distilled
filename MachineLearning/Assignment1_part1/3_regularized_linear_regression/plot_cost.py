import matplotlib.pyplot as plt
import os

def plot_cost(cost,alpha,lambda_value):
    
    fig, ax1 = plt.subplots()
    ax1.set_xlabel('Iterations')
    ax1.set_ylabel('Cost')
    plt.plot(cost)
    fig.tight_layout()
    plot_filename = os.path.join(os.getcwd(), 'figures', 'alpha:{}-lambda:{}-cost.png').format(alpha,lambda_value)
    plt.savefig(plot_filename)
    plt.show()
    plt.close()
