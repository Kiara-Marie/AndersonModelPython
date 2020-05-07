import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import scipy.stats
import config


class LevelSpacingStats:

  def __init__(self, num_sites, iterations):
    self.NUM_TO_SAVE = 100000
    self.num_sites = num_sites
    self.iterations = iterations
    self.spacings = np.empty(self.NUM_TO_SAVE)
    self.spacings[:] = np.NaN
    self.currPos = 0

  def save(self, eigvals, eigvecs, hamiltonian):
    diffs = eigvals[1:] - eigvals[0:-1]
    if ((len(diffs) + self.currPos) < self.NUM_TO_SAVE):
        self.spacings[self.currPos:(self.currPos + len(diffs))] = diffs
        self.currPos = self.currPos + len(diffs)
        if (self.currPos != self.NUM_TO_SAVE and 
            (not np.isnan(self.spacings[self.currPos]) 
             or np.isnan(self.spacings[self.currPos - 1]))):
          raise Exception("Something went wrong in level spacings")
            
  def printResult(self, file_code):
    filename = file_code + "-LevelSpacings.csv"
    df = pd.DataFrame(self.spacings)
    df.dropna(inplace=True)
    df.to_csv(filename, index=False)
    self.plotDistributions(df.to_numpy(), file_code)

  def plotDistributions(data, file_code):
    numBins = 20
    otherDistGran = 0.05
    mylinewidth = 3
    
    n,bins,patches = plt.hist(data, bins=numBins,density=True)

    D = np.mean(data)

    x = np.arange(0,np.max(bins),otherDistGran/np.max(bins))

    wigner = ((np.pi * x) / (2*D*D))*np.exp((-np.pi/4)*(np.square(x)/(D*D)))
    plt.plot(x,wigner,label='wigner',linewidth=mylinewidth)

    poisson = (1/D)*np.exp(-x/D)
    plt.plot(x,poisson,label='poisson',linewidth=mylinewidth)
        
    plt.legend(loc='upper right')
    plt.title('Distribution of Spacing to Closest Energy')
    
    plt.savefig(file_code + "-LevelSpacingDistribution.svg")

    # make sure you don't call show before you call save
    if (config.SHOW):
      plt.show()

      


