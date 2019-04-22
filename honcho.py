## gonna try to make a neural net lol ##

import numpy as np
import bot

class Honcho(bot.Bot):
    'Eural net.'
    # sigmoid function
    def nonlin(x,deriv=False):
        if(deriv==True):
            return x*(1-x)
        return 1/(1+np.exp(-x))
    
    def getMove(self, boardArr):
        # input dataset
        input_data = []
        for row in boardArr:
            for entry in row:
                if entry[0]>0:
                    input_data.append(1)
                else:
                    input_data.append(0)
                if entry[1]>0:
                    input_data.append(1)
                else:
                    input_data.append(0)
        print input_data

        X = np.array([input_data])
        
        # output dataset            
        #y = np.array([[0,0,1,1]]).T

        # seed random numbers to make calculation
        # deterministic (just a good practice)
        np.random.seed(1)

        # initialize weights randomly with mean 0
        syn0 = 2*np.random.random((200,200)) - 1

        print syn0

        l0 = X
        l1 = np.dot(l0,syn0)

        best = 0
        bestIndex = 0
        for i,row in enumerate(np.nditer(l1)):
            if row>best:
                best = row
                bestIndex = i
        row = bestIndex/19
        col = bestIndex%19/2
        direction = (bestIndex%2 + row%2 + 1)%2
        return (row, col, direction)


        #for iter in xrange(1000):

            # forward propagation
            #l0 = X
            #l1 = nonlin(np.dot(l0,syn0))

            # how much did we miss?
            #l1_error = y - l1

            # multiply how much we missed by the 
            # slope of the sigmoid at the values in l1
            #l1_delta = l1_error * nonlin(l1,True)

            # update weights
            #syn0 += np.dot(l0.T,l1_delta)
            
        return (0,0,0)

