import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

class Data:
    x_values = []                   #list of values for input
    y_values = []                   #list of values for output
    x = None                        #Input values in dataframe
    y = None                        #Output values in dataframe
    df = None                       #Full dataframe
    fig = plt.figure()              #matplotlib figure
    InputOutputVariables = []       #Names of the variables of the data

    def __init__(self,df, InputOutputVariables):
        self.df = df
        self.x = df.loc[: , 'X1':'X8']
        self.y = df.loc[: ,'Y1':'Y2']
        self.x_values = self.x.values
        self.y_values = self.y.values
        self.InputOutputVariables = InputOutputVariables

    def plotInputScatterMatrix(self):
        pd.plotting.scatter_matrix(self.x,alpha=0.2,marker='*')

    def plotData(self,x,y,subplotNumber):
        ax = self.fig.add_subplot(331+subplotNumber)
        ax.grid(color='lightgray', linestyle='-', linewidth=1)
        ax.set_axisbelow(True)
        ax.scatter(x, y,color='red', alpha=.1, s=140, marker='.')
        ax.set_xlabel('x'+str(subplotNumber+1))
        ax.set_ylabel('y1')
        plt.savefig('plot_scatter2D.png')

    def plotAllInputOutput(self):
        for i in range(8):
            self.plotData(self.x_values[:,i],self.y_values[:,0],i)
        plt.show()
    
    def splitDataToTrainAdndTest(self):
        train, test = train_test_split(self.df, test_size=0.35)
        train_x = train.loc[: , 'X1':'X8']
        train_y = train.loc[: ,'Y1':'Y2']
        test_x = test.loc[: , 'X1':'X8']
        test_y = test.loc[: ,'Y1':'Y2']
        return (train_x, train_y, test_x, test_y)