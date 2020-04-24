import numpy as np
import pandas as pd

class SampleResults:

  def __init__(self, num_sites, iterations, num_samples = 3):
      self.num_sites = num_sites
      self.num_samples = min(num_samples, iterations)
      self.samples = []
      self.samples_so_far = 0


  def save(self, eigvals, eigvecs, hamiltonian):
      if (self.samples_so_far < self.num_samples):
          curr_sample = pd.DataFrame(columns=["Hamiltonian","Eigenvalues","Eigenvectors"])
          curr_sample["Hamiltonian"] = pd.Series(hamiltonian)
          curr_sample["Eigenvalues"] = eigvals
          curr_sample["Eigenvectors"] = pd.Series(eigvecs)
          self.samples.append(curr_sample)

            
  def printResult(self, file_code):
    filename = file_code + "-Samples.csv"
    df = pd.DataFrame(self.samples)
    df.to_csv(filename)
      


