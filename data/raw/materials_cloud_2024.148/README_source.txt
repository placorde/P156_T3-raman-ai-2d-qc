The data is stored in the `data` folder, where the naming convention for each folder is `<uniqueID>_<formula>`. Each folder contains three files:

- `geometry.in`: The input file accepted by the FHI-aims software we use, which saves the molecular structure information.
- `POSCAR`: The structure file in vasp format.
- `raman.dat`: The calculation result. In the file ramen.dat, the first column represents the frequency of the Raman spectrum in cm^-1; the second column represents the Raman intensity in Angstrom4/amu.