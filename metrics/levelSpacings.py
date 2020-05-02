import numpy as np
import pandas as pd

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
    df.dropna()
    df.to_csv(filename, index=False)
      


