import numpy as np

class Adaline:

    '''
    Building the Adaline model from scratch with gradient descent(batch gradient boost)
    '''
    
    def __init__(self, eta: float = 0.001, epochs: int = 50, random_state = 1):

        self.eta = eta
        self.epochs = epochs
        self.random_state = random_state

    def fit(self, x, y):

        self.costs = []

        rgen = np.random.RandomState(self.random_state)
        self.weights = rgen.normal(loc=0.0, scale=0.1, size= x.shape[1]+1)

        for i in range(self.epochs):

            net_input = self.net_computaion(x)
            output = self.activation(net_input)
            error = y-output
            self.weights[1:] += self.eta* np.transpose(x).dot(error)
            self.weights[0] += self.eta*error.sum()

            cost = float(round((error**2).sum()/2, 2))
            self.costs.append(cost)

            if i%10 == 0:
                print(f'Epochs: {i}, loss: {cost}')

        return self

    def activation(self, x):
        # Computing the linear activating function

        return x

    def net_computaion(self, X):
        return np.dot(X, self.weights[1:])+self.weights[0]

    def predict(self, x):
        return np.where(self.net_computaion(x) >= 0.0, 1, -1)
    

class Stochastic_Adaline:

    'Adaline with stochastic gradient boosting'

    def __init__(self, eta: float = 0.001, random_state = 1, epochs = 50):

        self.eta = eta
        self.random_state = random_state
        self.epochs = epochs
        self.init_weights = False


    def fit(self, X, Y):

        self._intitialize_weight(X)

        self.costs = []
        for _ in range(self.epochs):
            cost = 0
            X, Y= self._shuffle(X, Y)
            for xi, yi in zip(X, Y):
                cost += self._update_weights(xi, yi)
            
            self.costs.append(cost/len(Y))


    def _intitialize_weight(self, x):

        self.rgen = np.random.RandomState(self.random_state)
        self.weights = self.rgen.normal(loc=0, scale=0.1, size= 1+ x.shape[1])
        self.init_weights = True

    def _update_weights(self, x, y):

        net_input = self._net_input(x)
        op = self._activation(net_input)
        error = y-op

        self.weights[1: ] += self.eta*x.dot(error)
        self.weights[0] += self.eta*error

        cost = (error**2) * 0.5
        return cost
    
    def predict(self, x):
        return np.where(self._activation(self._net_input(x)) >=0 , 1, -1)
        
    def partial_fit(self, x, y):

        if not self.init_weights:
            self._intitialize_weight(x)
        if y.ravel().shape[0] >1:
            for xi, yi in zip(x, y):
                self._update_weights(xi, yi)
        else:
            self._update_weights(x, y)

    def _activation(self, x):
        # Linear activation function
        return x
    
    def _shuffle(self, x, y):
        shuffle = self.rgen.permutation(len(y))
        return x[shuffle], y[shuffle]
    
    def _net_input(self, x):
        return np.dot(x, self.weights[1: ])+ self.weights[0]
    