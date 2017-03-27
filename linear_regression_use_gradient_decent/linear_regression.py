import numpy as np
import pylab
def compute_error(b,m,data):
    
    totalError = 0

    for i in range(0,len(data)):
        x = data[i,0]
        y = data[i,1]

        totalError += (y-(m*x+b))**2

    return totalError/float(len(data))

def optimizer(data,starting_b,starting_m,learning_rate,num_iter):
    b = starting_b
    m = starting_m

    #gradient descent
    for i in range(num_iter):
        # thie gradient step
        b,m =step_gradient(b,m,data,learning_rate)
        if i%100==0:
            print 'iter {0}:error={1}'.format(i,compute_error(b,m,data))
    return [b,m]

def step_gradient(b_current,m_current,data ,learning_rate):

    b_gradient = 0
    m_gradient = 0

    N = float(len(data))

    for i in range(0,len(data)):
        x = data[i,0]
        y = data[i,1]

        #computing partial derivations of error function
        #b_gradient = -(2/N)*sum((y-(m*x+b))^2)
        #m_gradient = -(2/N)*sum(x*(y-(m*x+b))^2)
        b_gradient += -(2/N)*(y-((m_current*x)+b_current))
        m_gradient += -(2/N) * x * (y-((m_current*x)+b_current))

        #update our b and m values using out partial derivations

    new_b = b_current - (learning_rate * b_gradient)
    new_m = m_current - (learning_rate * m_gradient)
    return [new_b,new_m]


def plot_data(data,b,m):

    #plottting
    x = data[:,0]
    y = data[:,1]
    y_predict = m*x+b
    pylab.plot(x,y,'o')
    pylab.plot(x,y_predict,'k-')
    pylab.show()


def Linear_regression():
    # get train data
    data =np.loadtxt('./data/data.csv',delimiter=',')

    # define hyperparamters
    #learning_rate is used for update gradient
    learning_rate = 0.001

    # define  y =mx+b
    initial_b =0.0
    initial_m = 0.0

    #defint the number that will iteration
    num_iter = 1000

    # train model
    #print b m error
    print 'initial variables:\n initial_b = {0}\n intial_m = {1}\n error of begin = {2} \n'\
        .format(initial_b,initial_m,compute_error(initial_b,initial_m,data))

    #optimizing b and m
    [b ,m] = optimizer(data,initial_b,initial_m,learning_rate,num_iter)

    #print final b m error
    print 'final formula parmaters:\n b = {1}\n m={2}\n error of end = {3} \n'.format(num_iter,b,m,compute_error(b,m,data))

    #plot result
    plot_data(data,b,m)

if __name__ =='__main__':

    Linear_regression()
