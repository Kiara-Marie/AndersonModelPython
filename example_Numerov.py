# -*- coding: utf-8 -*-
"""
Created on Tue May 19 17:56:38 2020

@author: User
"""

## Numerov method: M. L. Zimmerman, M. G. Littman, M. M. Kash, and D. Kleppner, Phys. Rev. A 20, 2251 (1979).
## https://pairinteraction.github.io/pairinteraction/sphinx/html/wavefunctions.html#numerovs-method-and-model-potentials
from class_Numerov import Numerov
 
d=Numerov().Rad_int(10,9,10,8) # (n1,l1,n2,l2,p=1), p is the order of <n1,l1| r^p |n2,l2>; d is in atomic unit

# The dipole moment is ed = e<n1,l1|r|n2,l2>. Let us ignore constant e for now

print(d)