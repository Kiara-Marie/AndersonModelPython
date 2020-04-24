import numpy as np
import scipy
import scipy.linalg
import config

class Simulation:

  def __init__(self, W, iterations, num_sites, max_t, jComputer, 
               energyComputer, metrics):
    self.W = W 
    self.iterations = iterations
    self.num_sites = num_sites
    self.max_t =  max_t
    self.jComputer = jComputer
    self.energyComputer = energyComputer
    self.metrics = metrics

  def run(self):
    for iter in range(self.iterations):
      hamiltonian = self.createMatrix()
      eigvals, eigvecs = scipy.linalg.eigh(
          hamiltonian, check_finite=config.CAREFUL, turbo=True)
      for m in self.metrics:
          m.save(eigvals, eigvecs, hamiltonian)
    for m in self.metrics:
        m.printResult()


  def createMatrix(self):
    energies = self.energyComputer.getEnergies()

    hamiltonian = np.diag(energies)

    for xi in range(self.num_sites):
      for xj in range(xi, self.num_sites):
        if (xi == xj):
          continue
        j = self.jComputer.jFinder(xi,xj)
        hamiltonian[xi,xj] = j
        hamiltonian[xj,xi] = j

    if (config.CAREFUL and not (check_symmetric(hamiltonian))):
      raise Exception("Hamiltonian was not symmetric!")

    return hamiltonian


   # from https://stackoverflow.com/questions/42908334/checking-if-a-matrix-is-symmetric-in-numpy
  def check_symmetric(a, rtol=1e-05, atol=1e-08):
    return np.allclose(a, a.T, rtol=rtol, atol=atol)

