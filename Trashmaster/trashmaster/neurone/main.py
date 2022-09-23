import pybrain3
import pickle
import matplotlib.pylab as plt
from numpy import ravel
from pybrain3.tools.shortcuts import buildNetwork
from pybrain3.datasets import SupervisedDataSet
from pybrain3.supervised.trainers import BackpropTrainer 
from pybrain3.tools.xml.networkwriter import NetworkWriter
from pybrain3.tools.xml.networkreader import NetworkReader

# https://www.machinelearningmastery.ru/how-to-configure-the-number-of-layers-and-nodes-in-a-neural-network/
class SupervisedDataSetModel():
    def __init__(self, metrics:int = 4, 
                 predictions:int = 1, 
                 input_layer:int = 4, 
                 hidden_layer:int = 3,
                 output_layer:int = 1):
        # 4 метрики, 1 предикшн
        self.metrics = metrics
        self.predictions = predictions
        self.input_layer = input_layer
        self.hidden_layer = hidden_layer
        self.output_layer = output_layer
        self.ds = SupervisedDataSet(metrics, predictions)
        
    
    def activateModel(self):
        self.net = buildNetwork(self.input_layer, self.hidden_layer, self.output_layer, bias=True)
        self.trainer = BackpropTrainer(self.net, dataset=self.ds, momentum=0.1, learningrate=0.01, verbose=True, weightdecay=0.01)

        self.trnerr, self.valerr = self.trainer.trainUntilConvergence()
        
        plt.plot(self.trnerr, 'b', self.valerr, 'r')
        plt.show()

    def addDataToModel(self, input:list, target:list):
        self.ds.addSample(inp=input, target=target)
    
    def predict(self, data:list):
        y = self.net.activate(data)
        print(y)
        return y
    
    def saveModel(self):
        fileObject = open('model.txt', 'wb') 
        pickle.dump(self.net, fileObject) 
        fileObject.close()
        

def getModel():
        fileObject = open('model.txt', 'rb') 
        net2 = pickle.load(fileObject) 
        fileObject.close()
        return net2
    
model = SupervisedDataSetModel()

# model.addDataToModel([2, 3, 80, 1], [5])
# model.addDataToModel([5, 5, 50, 2], [4])
# model.addDataToModel([10, 7, 40, 3], [3])
# model.addDataToModel([15, 9, 20, 4], [2])
# model.addDataToModel([20, 11, 10, 5], [1])

# model.activateModel()

# model.saveModel()

# USE MODEL - >
model = getModel()
print(model.activate([2, 3, 80, 1]))

