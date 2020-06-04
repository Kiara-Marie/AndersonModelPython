import numpy as np
import argparse

import config

from simClass import Simulation
from jComputers import constant, lorentz
from energyComputers import uniformRandom, calculatedRandom, sumOnsitesDecorator
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
  config.SHOW = vars(result)['show']
  config.SAVE = vars(result)['save']
  config.SEED = vars(result)['seed']

  print("Running %d iterations for %d sites with W = %d, and max_t = %f" %(iterations,num_sites, W, max_t))

  energy_computer = sumOnsitesDecorator.SumOnsitesDecorator(calculatedRandom.CalculatedRandomEnergies(num_sites))
  
  jComputer = lorentz.Lorentz(nnOnly=True, t=max_t, rdep=True, energy_computer=energy_computer, gamma=1)
  level_spacings = levelSpacings.LevelSpacingStats(num_sites, iterations)
  sample_results = sampleResults.SampleResults(num_sites, iterations)
  metrics = [level_spacings, sample_results]

  curr_sim = Simulation(W=W, iterations=iterations, num_sites=num_sites,
                       max_t=max_t, jComputer=jComputer, 
                       energy_computer=energy_computer, metrics=metrics)

  curr_sim.run()


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
                        action='store', default=True)
  
  parser.add_argument('--show', type=bool, nargs='?',
                        help = 'Whether to show any plots that are generated',
                        action='store', default=True)
  parser.add_argument('--save', type=bool, nargs='?',
                        help = 'Whether to save results to file',
                        action='store', default=True)
  parser.add_argument('--seed', type=int, nargs='?',
                        help="Seed to provide to random number generator",
                        action='store', default=None)

  result = parser.parse_args()
  return result

main()
    
