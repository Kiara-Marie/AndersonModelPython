import numpy as np
#import config
#from numpy.random import default_rng
from energyComputers.randomRydbergs import RandomRydbergs

class PenningRydbergs(RandomRydbergs):
  def __init__(self,num_sites):
    super().__init__(num_sites)  
    self.desc= "Each site randomly assigned pqn_0 level from empirical distribution, \
      then pqn_f level, such that pqn_0 + MIN_JUMP <= pqn_f <= pqn_0 + MAX_JUMP \
      then choosing l_0 and l_f from random uniform distribution over allowed values based on \
      the values of pqn_0 and pqn_f. Onsite energy is equal to the energy gap between the initial \
      and final state, in units of ____ \n"

  def get_ns_and_ls(self):
    pdf = self.penning_distr()
    
#    self.n0s=np.random.choice(self.ns, self.num_sites, p=pdf)  #sample the first pqns
#    np.rint(self.n0s, out=self.n0s)
    n0s=np.zeros(self.num_sites,dtype=int)
    l0s=np.zeros(self.num_sites,dtype=int)
    nfs=np.zeros(self.num_sites,dtype=int)
    lfs=np.zeros(self.num_sites,dtype=int)
    #need a for loop here 
    # NOTE FROM KIARA: I think we should be able to do this without a for-loop
    for xi in range(self.num_sites):
        n0s[xi]=np.random.choice(self.ns, 1, p=pdf) #sample pqn of initial state 
        l0s[xi]=np.random.choice(n0s[xi], 1) #uniform sample from l= 0 to n0-1
        # NOTE FROM KIARA: Why can't we just pick a jump from a uniform distribution?
        nfs[xi]=np.random.choice(self.ns, 1, p=self.second_distr(n0s[xi])) #sample pqn of final state near the initial state 
        # NOTE FROM KIARA: Spectroscopic transition rules mean that delta(l) = (+/-)1, right?
        lfs[xi]=np.random.choice(nfs[xi], 1) #uniform sample from l= 0 to nf-1
    self.n0s=n0s
    self.l0s=l0s
    self.nfs=nfs
    self.lfs=lfs
    

    
  def penning_distr(self, pqn0=50, penning_fraction=0.5): # penningfraction can be a function of n0. we can set it 0.5 for now.
      
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
      self.pdf=nden/np.sum(nden)
     
      return self.pdf  # return the probalility distribution function over n's from MIN_N to MAX_N
      
  def second_distr(self, nearby_n0):
      
      orginal_pdf=self.pdf
      n1=nearby_n0-self.MAX_JUMP
      n2=nearby_n0-self.MIN_JUMP #Lower allowed region
      
      n3=nearby_n0+self.MIN_JUMP
      n4=nearby_n0+self.MAX_JUMP # higher allowed region     
      
      filt=(self.ns >= n1) & (self.ns <= n2) & (self.ns >= n3) & (self.ns <= n4)
      
      new_pdf=orginal_pdf*filt  #allow only states around nearby_n0
      self.second_pdf=new_pdf/np.sum(new_pdf) # norm to 1
      return self.second_pdf
      
      
      
  
    
    
    
    
    
    
    
    
