# Molecular-dynamics-Interaction-plot
Two scripts for MD interaction analysis (similar to interaction fraction on Desmond).

How to use:
1. Set your pdb_file_name and ligand_code on the "run_interact.sh".
2. Run "run_interact.sh" where your pdb file is located.
3. Run "run_interact.sh" in the same directory.

How the script works:
The analysis is based on a *.pdb file that contains "n" number of frames from a MD.
PLIP analysis is performed to determine the type of interactions for each frame.
Data is concatenated and sorted for appropriate plotting.
