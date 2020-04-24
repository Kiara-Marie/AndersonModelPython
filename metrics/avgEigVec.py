import numpy as np
import pandas as pd

class AvgEigVec:
  
  def __init__(self, num_sites, iterations):
    self.avg_mat = np.zeros(num_sites)
    self.num_sites = num_sites
    self.iterations = iterations

  def save(self, eigvals, eigvecs, hamiltonian):
    np.add(self.avg_mat, eigvecs, out=self.avg_mat)
  
  def printResult(self, file_code):
    filename = file_code + "-AverageEigenvectors.csv"
    np.multiply(self.avg_mat, (1/self.iterations), out=self.avg_mat)
    df = pd.DataFrame(self.avg_mat)
    df.to_csv(filename)