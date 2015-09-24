import pandas as pd
import matplotlib.pyplot as plt

#globals
fileName = "./USD.csv"

class fileLoader:
#Loads data from csv file into pandas data frame.
    
    fileToLoad = None
    data = None
    csvSeparator = ";"
    
    def __init__(self, fName = fileName):
    #Set filename and load data
        self.setFile(fileName)
        self.loadData()
        
    
    def setFile(self, fileName):
    #set filename for loading data
        self.fileToLoad = fileName
        
    def loadData(self):
    #load data from file
        self.data = pd.read_csv(self.fileToLoad, \
                                sep=self.csvSeparator)
        
    def getData(self):
    #return data to user
        return self.data

class bollingerCalculator:
    
    #periods for rolling mean and standard deviation
    mPeriods = 0
    sPeriods = 0
    
    #number if standard deviations band lies above/
    #below mean
    sMultiple = 1.5
    
    #member to store input data
    data = None
    
    #dictionary to store computation results
    results = {}
    
    def __init__(self, inputData = None, meanPeriods = 50, stdPeriods = 50, stdMultiple = 1.5):
        self.mPeriods = meanPeriods
        self.sPeriods = stdPeriods
        self.sMultiple = stdMultiple
        self.setData(inputData)
        self.compute()        

    def setData(self, inputData):
        self.data = inputData
            
    def compute(self):
        if type(self.data) == pd.core.series.Series:
            
            #set basic series
            self.results["data"] = self.data
            print self.results
            
            #compute rolling std, rolling mean
            self.results["rollingMean"] = pd.rolling_mean(self.data, self.mPeriods)        
            self.results["rollingStd"] = pd.rolling_std(self.data, self.sPeriods)
            
            #compute bollinger bands
            self.results["upperBand"] = self.results["rollingMean"] + self.sMultiple*self.results["rollingStd"]
            self.results["lowerBand"] = self.results["rollingMean"] - self.sMultiple*self.results["rollingStd"]
            
        else:
            print "bollingerCalculator::Input data must"
            print "be of type pd.core.series.Series."
            print "Use '.setData to set input data."
        
    def __getitem__(self, item):
        return self.results[item]

        
if __name__=="__main__":
    #main loop

    #
    #parameters
    #
    
    #path and filename for data file
    fileToLoad = "./USD.csv"    
    
    #name of column to analyse
    colName = "USD.Close"
    
    #bollinger band parameters
    bol_meanPeriods = 100
    bol_stdPeriods = 100
    bol_stdMultiple = 1.5

    #
    #load data and calculate
    #
    
    #load data from file
    fLoader = fileLoader(fileName)
    data = fLoader.getData()

    #make bollinger band calculator
    bCalculator = bollingerCalculator( \
        inputData = data[colName], \
        meanPeriods = bol_meanPeriods, \
        stdPeriods = bol_stdPeriods, \
        stdMultiple= bol_stdMultiple)    


    #
    #plot results
    #

    plt.plot(bCalculator["upperBand"])
    plt.plot(bCalculator["lowerBand"])
    plt.plot(bCalculator["rollingMean"])
    plt.plot(bCalculator["data"])
    plt.show()    

 
