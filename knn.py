import numpy as np
import time
import random
import scipy.stats as ss
import matplotlib.pyplot as plt
import datagenerator

def plot_prediction_grid (xx, yy, prediction_grid, points):
    """ Plot KNN predictions for every point on the grid."""
    from matplotlib.colors import ListedColormap
    background_colormap = ListedColormap (["hotpink","lightskyblue", "yellowgreen","violet"])
    observation_colormap = ListedColormap (["red","blue","green","indigo"])
    plt.figure(figsize =(10,10))
    plt.pcolormesh(xx, yy, prediction_grid, cmap = background_colormap, alpha = 0.5)
    plt.scatter(points[:,0], points [:,1], c = outcomes, cmap = observation_colormap, s = 50)
    plt.xlabel('Variable 1'); plt.ylabel('Variable 2')
    plt.xticks(()); plt.yticks(())
    plt.xlim (np.min(xx), np.max(xx))
    plt.ylim (np.min(yy), np.max(yy))
    #plt.savefig(filename)
    plt.show()

def euclidean_distance(p1,p2):
    """ to calculate euclidean distance using formula squareroot((x1-x2)^2 + (y1-y2)^2)"""
    return(np.linalg.norm(p1-p2))

def majority_vote(votes):
    """ picks the most common element from the array"""
    votes_count = dict()
    for vote in votes:
        if vote in votes_count:
            votes_count[vote] += 1
        else:
            votes_count[vote] = 1
    
    max_vote = max(votes_count.values())
    winners = [key for key,value in votes_count.items() if value == max_vote]
    return (random.choice(winners),max_vote)

def majority_vote_scipy(votes):
    """ picks the most common element from the array using scipy module"""
    winner,count = ss.mstats.mode(votes)
    return(winner,count)

def find_k_nearest_neighbour(test_point,points,k=3):    
    distances = np.array([euclidean_distance(test_point,p) for p in points])
    sorted_indices = np.argsort(distances)
    return(sorted_indices[:k])

def knn_predict(test_point,points,outcomes,k):
    k_n_n = find_k_nearest_neighbour(test_point,points,k)
    return(majority_vote(outcomes[k_n_n]))


def make_prediction_grid(points, outcomes, limits, h, k):
    """ function to create a prediction meshgrid"""
    (x_min, x_max, y_min, y_max) = limits
    xs = np.arange(x_min, x_max, h)
    ys = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs, ys)

    prediction_grid = np.zeros(xx.shape, dtype=int)

    for i,x in enumerate(xs):
        for j,y in enumerate(ys):
            prediction_grid[j,i] = knn_predict(np.array([x,y]), points, outcomes, k)[0]

    return (xx, yy, prediction_grid)

p1 = np.random.randn(2,3)
p2 = np.random.randn(2,3)

outcomes = np.array([1,2,3,1,2,3,3,2,1])
points = np.random.randn(9,2)
p = [.023,0.572]
points, outcomes = datagenerator.generate_bivariant_data(100, 4)

limits = (np.min(points[:,0]),np.max(points[:,0]),np.min(points[:,1]),np.max(points[:,1]))
xx, yy, prediction_grid = make_prediction_grid(points,outcomes,limits,.1,30)
plot_prediction_grid(xx, yy, prediction_grid, points)




