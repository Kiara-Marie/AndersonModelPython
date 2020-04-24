import numpy as np
import scipy as scipy
import argparse

import config

from simClass import Simulation
from jComputers import constant
from energyComputers import uniformRandom
from metrics import levelSpacings, sampleResults

def main():

  W_default = 5
  iterations_default = 10
  num_sites_default = 20
  max_t_default = 3

  result = get_settings(W_default, iterations_default, num_sites_default, max_t_default)
  W = vars(result)['W']
  iterations = vars(result)['i']
  num_sites = vars(result)['s']
  max_t = vars(result)['mt']
  config.CAREFUL = vars(result)['c']

  print("Running %d iterations for %d sites with W = %d, and max_t = %d" %(iterations,num_sites, W, max_t))

  jComputer = constant.Constant(nnOnly=True, t=max_t, rdep=True)

  energyComputer = uniformRandom.UniformRandomEnergies(W, num_sites)
  
  level_spacings = levelSpacings.LevelSpacingStats(num_sites, iterations)
  sample_results = sampleResults.SampleResults(num_sites, iterations)
  metrics = [level_spacings, sample_results]
  
  currSim = Simulation(W=W, iterations=iterations, num_sites=num_sites,
                       max_t=max_t, jComputer=jComputer, 
                       energyComputer=energyComputer, metrics=metrics)
  currSim.run()


def get_settings(W_default, iterations_default, num_sites_default, max_t_default):
  
  parser = argparse.ArgumentParser(description='Run the Anderson model as set up in main.py')
  parser.add_argument('--W', type=int, nargs='?',
                      help='The integer degree of disorder', action='store', default=W_default)

  parser.add_argument('--i','--iterations', type=int,nargs='?', 
                      help='Number of matrices to generate and diagonalize', action='store', default=iterations_default)

  parser.add_argument('--s','--num_sites', type=int, nargs='?',
                      help ='Number of lattice sites', action='store', default=num_sites_default)

  parser.add_argument('--mt','--max_t', type=float, nargs='?',
                        help='Maximum value of t used to scale hopping amplitude J', action='store', default=max_t_default)

  parser.add_argument('--c', '--careful', type=bool, nargs='?',
                        help = 'Whether to run extra (time consuming) checks to verify code is working properly', 
                        action='store', default=False)

  result = parser.parse_args()
  return result

main()
    
