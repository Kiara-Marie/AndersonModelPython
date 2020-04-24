import numpy as np

class LevelSpacingStats:

  def __init__(self, num_sites, iterations):
    self.NUM_TO_SAVE = 100000
    self.num_sites = num_sites
    self.iterations = iterations
    self.spacings = []

  def save(self, eigvals, eigvecs, hamiltonian):
    # TODO
    diffs = eigvals[1:] - eigvals[0:-1]
    if (len(diffs) + len(self.spacings) < self.NUM_TO_SAVE):
      self.spacings.append(diffs)


