import numpy as np
import scipy
import scipy.linalg
import config
import datetime as datetime

from aboutRun import about_run

class Simulation:

  def __init__(self, W, iterations, num_sites, max_t, jComputer, 
               energy_computer, metrics):
    self.W = W 
    self.iterations = iterations
    self.num_sites = num_sites
    self.max_t =  max_t
    self.jComputer = jComputer
    self.energy_computer = energy_computer
    self.metrics = metrics

  def run(self):
    for iter in range(self.iterations):
      hamiltonian = self.createMatrix()
      eigvals, eigvecs = scipy.linalg.eigh(
          hamiltonian, check_finite=config.CAREFUL, turbo=True)
      for m in self.metrics:
          m.save(eigvals, eigvecs, hamiltonian)
    run_code = self.get_run_code()
    file_prefix = "results/" + run_code
    about_run(W=self.W, iterations=self.iterations, num_sites=self.num_sites,
              max_t=self.max_t, jComputer=self.jComputer, 
              energy_computer=self.energy_computer, file_prefix=file_prefix)
    for m in self.metrics:
        m.printResult(file_prefix)


  def createMatrix(self):
    energies = self.energy_computer.get_energies()

    hamiltonian = np.diag(energies)

    for xi in range(self.num_sites):
      for xj in range(xi, self.num_sites):
        if (xi == xj):
          continue
        j = self.jComputer.jFinder(xi,xj)
        hamiltonian[xi,xj] = j
        hamiltonian[xj,xi] = j

    if (config.CAREFUL and not (self.check_symmetric(hamiltonian))):
      raise Exception("Hamiltonian was not symmetric!")

    return hamiltonian


   # from https://stackoverflow.com/questions/42908334/checking-if-a-matrix-is-symmetric-in-numpy
  def check_symmetric(self, a, rtol=1e-05, atol=1e-08):
    return np.allclose(a, a.T, rtol=rtol, atol=atol)

  def get_run_code(self):
    currentDT = datetime.datetime.now()
    return "%d_%d_%d_%d_%d_%d" % (currentDT.year, currentDT.month, currentDT.day, currentDT.hour, currentDT.minute, currentDT.second)

