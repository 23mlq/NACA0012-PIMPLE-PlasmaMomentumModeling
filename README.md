

Created on Fri June 20 2025

@author: 23mlq


Simulation to investigate effects of plasma DBD actuators on an
airfoil at Low Reynolds number, including laminar separation bubbles.
kOmegaSST model captures LSBs but fails to predict stall and
over predicts lift past 10 degrees. Transition Model may be more
accurate but was not investigated. Plasma region is modelled using
topoSetDict as a rotatedBoxToCell, body force modelled using fvOptions
through vectorSemiImplicit with a time varying force by inputting
magnitude of force in a table. Simulations conducted with and without
plasma. Mesh created through ANSYS Fluent. 


- NACA0012 Airfoil
- Chord length 0.1m
- Re = 53,000
- FreeStreamVelocity = 7.95m/s
- rhoInf = 1.0
- Nu = 1.50e-05;
- 2D Incompressible PIMPLE solver in PISO mode
- RAS: kw-SST and kOmegaSSTLM
- MaxCo = 1.0
- 2sec simulation time
- wall y+ average ~3
- wall y+ max ~ 8


Currently set to 10 AOA. To vary AOA, modify
0/include/initialConditions and change freeStream x-y components.
Then modify system/forceCoeffs and modify lift, and drag x-y
components.

