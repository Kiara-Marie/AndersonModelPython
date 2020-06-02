import numpy as np
import pandas as pd
from abc import ABC
import config
from metrics.metric import Metric

class SampleResults(Metric):

  def __init__(self, num_sites, iterations, num_samples = 3):
      super().__init__(num_sites, iterations)
      self.num_samples = min(num_samples, iterations)
      self.samples = pd.DataFrame()
      self.samples_so_far = 0
      hamiltonian_headers = ["Hamiltonian_col%d" % (d) for d in range(self.num_sites)]
      eigvals_header = ["Eigenvalues"]
      eigvecs_header = ["Eigenvector_col%d" % (d) for d in range (self.num_sites)]
      self.headers = hamiltonian_headers + eigvals_header + eigvecs_header


  def save(self, eigvals, eigvecs, hamiltonian):
      if (self.samples_so_far < self.num_samples):
          eigvals = (eigvals[np.newaxis]).T
          concatResult = np.concatenate((hamiltonian, eigvals, eigvecs), axis=1)
          curr_sample = pd.DataFrame(data=concatResult, columns=self.headers)
          suffix = '_' + str(self.samples_so_far)
          if (self.samples_so_far == 0):
            self.samples = curr_sample
            self.samples_so_far = 1
          else:
            self.samples = self.samples.join(other=curr_sample, rsuffix=suffix)
            self.samples_so_far = self.samples_so_far + 1

            
  def printResult(self, file_code):
    filename = file_code + "-Samples.csv"
    if (config.SAVE):
      self.samples.to_csv(filename, index=False, header=True, sep=',', encoding ='utf-8')
    
      


