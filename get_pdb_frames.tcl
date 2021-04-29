###################################
#  By: Gustavo E. Olivos-Ramirez  #
#      gustavo.olivos@upch.pe     #
#      Lima-Peru                  #
###################################

mol new md_0_10.gro
animate delete beg 0 end 0
mol addfile {005_PS-002.xtc} type {xtc} first 0 last 9999 step 10 waitfor -1
#Para cargar un archivo pdb
#mol addfile {out_003_PS_PDBtrajectories.pdb} type {pdb} first 1 last 20002 step 10 waitfor -1
set sel [atomselect top "protein or resname UNK"]
animate write pdb {name.pdb} beg 0 end -1 sel $sel waitfor -1
#exit
