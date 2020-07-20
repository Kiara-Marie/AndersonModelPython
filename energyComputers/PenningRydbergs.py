import numpy as np
import config
from numpy.random import default_rng
from energyComputers.randomRydbergs import RandomRydbergs

class PenningRydbergs(RandomRydbergs):
  def __init__(self,num_sites):
    super().__init__(num_sites)  
    self.desc= "Each site randomly assigned pqn_0 level from empirical distribution, \
      then pqn_f level, such that pqn_0 + MIN_JUMP <= pqn_f <= pqn_0 + MAX_JUMP \
      then choosing l_0 and l_f from random uniform distribution over allowed values based on \
      the values of pqn_0 and pqn_f. Onsite energy is equal to the energy gap between the initial \
      and final state, in units of ____ \n"

  def get_ns_and_ls(self, upper_from_penning):
    pdf = self.penning_distr()
    self.n0s = self.rng.choice(self.ns, self.num_sites, p=pdf) #sample pqn of initial state 
    self.l0s = np.multiply(self.rng.random(size=self.num_sites),  self.n0s)

    if (upper_from_penning):
        self.nfs = np.zeros(self.num_sites)
        for xi in range(self.num_sites):
             #sample pqn of final state near the initial state
            self.nfs[xi]=self.rng.choice(self.ns, 1, p=self.penning_distr(min_pqn=self.n0s[xi])) 
    else:
        n_jumps = (self.MAX_JUMP - self.MIN_JUMP + 1) * self.rng.random(size=self.num_sites) + self.MIN_JUMP
        np.floor(n_jumps, out=n_jumps)
        self.nfs = self.n0s + n_jumps
    
    # sample from 0-1, round to either 0 or 1, turn 0's into -1's
    l_jumps = np.rint(self.rng.random(size=self.num_sites))
    l_jumps[l_jumps == 0] -= 1
    self.lfs = self.l0s + l_jumps     

  def penning_distr(self, pqn0=50, penning_fraction=0.5, min_pqn=0): # penningfraction can be a function of n0. we can set it 0.5 for now.
      
      self.pqn0=pqn0
      
      eden=penning_fraction/2; # electron produced per penning partner
      rden=1-penning_fraction # remaining Rydberg on pqn0 that is not penning ionized
      self.ns=np.arange(self.MIN_N,self.MAX_N+1)
      
      n_bound=np.int(pqn0/2**0.5)    
      ns_lower=np.arange(self.MIN_N,n_bound,dtype='int64') #allowed lower n states after penning ionization
      indx=range(ns_lower.size)
      x=ns_lower/pqn0

      nden=np.zeros(self.MAX_N-self.MIN_N+1) #initialize the distribution over n
      nden[indx]=eden*x**5/np.sum(x**5) #redistribute lower n's
      
      nden[self.ns==self.pqn0]=rden 
      pdf=nden/np.sum(nden)
      filt = pdf > min_pqn
      pdf = pdf*filt  #allow only states above min_pqn 

      # if no states are above min_pqn, then just make the only allowed state the max_n
      if (np.all(pdf == 0)):
          pdf[-1] = 1
      return pdf  # return the probalility distribution function over n's from MIN_N to MAX_N
      
      
      
  
    
    
    
    
    
    
    
    
