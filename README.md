# AndersonModelPython

## Structure

This model is meant to be a flexible command line tool that can be used to quickly consider different Anderson lattice Hamiltonians, and look at various metrics to understand their solutions. It is designed to be easily extended. 

```
│   .gitignore              // Just a typical .gitignore
│   aboutRun.py             // This allows each run to automatically document itself
│   config.py               // Global configuration variables set with command line arguments are stored here
│   main.py                 
│   simClass.py             // This does the actual work of creating and diagonalizing the matrices
|                           //  and sending results to metrics
│
├───energyComputers         // Folder for all of the energyComputers
|       energyComputer.py   // Abstract energyComputer class
│       uniformRandom.py    
│
├───jComputers              // Folder for all the jComputers
|       jComputer.py        // Abstract jComputer class
│       constant.py
│   
│
└───metrics                 // Folder for all the metrics
        metric.py           // Abstract metric class
        avgEigVec.py
        levelSpacings.py
        sampleResults.py
```        


From **main.py**, there are a number of components that determine what version of the model to use. Each component will be an instance of a corresponding abstract class. 

* Method to use for choosing onsite/diagonal entries in the Hamiltonian (see **energyComputer.py**) 
* Method to use for choosing off-diagonal entries (see **jComputer.py**)
* Metrics or types of analysis to save when considering the solutions (see **metric.py**)

When running the model from the command line, you can select

* Number of sites in the Anderson lattice
* Number of iterations to run (number of times to regenerate a random matrix and diagonalize it)
* A degree of disorder parameter, *W*, whose use depends on the choice of `energyComputer` in **main.py**
* A degree of coupling, *t*, whose use depends on the choice of `jComputer` in **main.py**

## Command line

When run from a python shell, you need simply run `main.py` with parameters as specified below. From general commandline, run `python main.py` and then your arguments
```
usage: main.py [-h] [--W [W]] [--i [I]] [--s [S]] [--mt [MT]] [--c [C]] [--show [SHOW]]

Run the Anderson model as set up in main.py

optional arguments:
  -h, --help            show this help message and exit
  --W [W]               The integer degree of disorder
  --i [I], --iterations [I]
                        Number of matrices to generate and diagonalize
  --s [S], --num_sites [S]
                        Number of lattice sites
  --mt [MT], --max_t [MT]
                        Maximum value of t used to scale hopping amplitude J
  --c [C], --careful [C]
                        Whether to run extra (time consuming) checks to verify code is working properly                     
  --show [SHOW]         Whether to show any plots that are generated
```
