import numpy as np

def generate_bivariant_data(n=50, classes = 2):
    """function to generate dataset from normal distribution"""
    cov = [[1, 0], [0, 5]]
    for class_ in range(classes):
        mean = [class_*2, class_]
        if (class_==0):
            data = np.random.default_rng().multivariate_normal(mean, cov,n)
            outcomes = np.repeat(class_,n)
        elif (class_> 0):
            data = np.concatenate((data,np.random.default_rng().multivariate_normal(mean, cov,n)),axis = 0)
            outcomes = np.concatenate((outcomes,np.repeat(class_,n)))
    return (data,outcomes)

def main():
    n = 50
    classes = 3
    data,outcomes = generate_bivariant_data(n, classes)
    import matplotlib.pyplot as plt
    plt.figure()
    plt.plot(data[:n,0], data[:n,1], "ro")
    plt.plot(data[n:n+n,0], data[n:n+n,1], "bo")
    plt.plot(data[n+n:,0], data[n+n:,1], "go")
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    main()