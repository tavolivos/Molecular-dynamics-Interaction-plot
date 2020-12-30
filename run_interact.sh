###################################
#  By: Gustavo E. Olivos-Ramirez  #
#      gustavo.olivos@upch.pe     #
#      Lima-Peru                  #
###################################

ligand_code=UNL
pdb=md_400_last.pdb
i=1
while read line; do
	echo "${line}" >> model_${i}.pdb 
	[[ ${line[0]} == END ]] && ((i++)) 
done < $pdb
for file in model_*; do
	mkdir ${file%.pdb} && mv ${file} ${file%.pdb};
done
for d in model_*; do
	cd ${d}
	plip -f model*.pdb -t -yv
	cd ../;
done
for d in */; do
        cd ${d}
        sed -n -e '/($ligand_code) - SMALLMOLECULE/,/SMALLMOLECULE/p' *.txt > all_interact.dat
	sed -i '$ d' all_interact.dat
	echo "**" >> all_interact.dat
        sed -i -z 's/+//g; s/-//g; s/=//g; s/|//g; s/*\*\n/\n/g' all_interact.dat
        awk '{print $1,$2}' all_interact.dat > res_interact.dat
#Hydrophobic
        sed -n -e '/Hydrophobic Interactions/,/*/p' res_interact.dat > hydrophobic.dat
        sed -i 's/ /-/g' hydrophobic.dat
        sed -i -z 's/\n\-//g' hydrophobic.dat
        sed -i 's/RESNR-RESTYPE//' hydrophobic.dat
        grep -v "\*" hydrophobic.dat > temp && mv temp hydrophobic.dat
        sed '/^$/d' hydrophobic.dat > temp && mv temp hydrophobic.dat
#H-bond
        sed -n -e '/Hydrogen Bonds/,/*/p' res_interact.dat > h_bond.dat
        sed -i 's/ /-/g' h_bond.dat
        sed -i -z 's/\n\-//g' h_bond.dat
        sed -i 's/RESNR-RESTYPE//' h_bond.dat
        grep -v "\*" h_bond.dat > temp && mv temp h_bond.dat
        sed '/^$/d' h_bond.dat > temp && mv temp h_bond.dat
#Salt-bridges
        sed -n -e '/Salt Bridges/,/*/p' res_interact.dat > salt_bridges.dat
        sed -i 's/ /-/g' salt_bridges.dat
        sed -i -z 's/\n\-//g' salt_bridges.dat
        sed -i 's/RESNR-RESTYPE//' salt_bridges.dat
        grep -v "\*" salt_bridges.dat > temp && mv temp salt_bridges.dat
        sed '/^$/d' salt_bridges.dat > temp && mv temp salt_bridges.dat
#pi-Stacking
        sed -n -e '/piStacking/,/*/p' res_interact.dat > pi_stacking.dat
        sed -i 's/ /-/g' pi_stacking.dat
        sed -i -z 's/\n\-//g' pi_stacking.dat
        sed -i 's/RESNR-RESTYPE//' pi_stacking.dat
        grep -v "\*" pi_stacking.dat > temp && mv temp pi_stacking.dat
        sed '/^$/d' pi_stacking.dat > temp && mv temp pi_stacking.dat
#pi-Cation
        sed -n -e '/piCation/,/*/p' res_interact.dat > pi_cation.dat
        sed -i 's/ /-/g' pi_cation.dat
        sed -i -z 's/\n\-//g' pi_cation.dat
        sed -i 's/RESNR-RESTYPE//' pi_cation.dat
        grep -v "\*" pi_cation.dat > temp && mv temp pi_cation.dat
        sed '/^$/d' pi_cation.dat > temp && mv temp pi_cation.dat
#Remove 
        cd ../;
done
for d in */; do
        cat ${d%/}/h_bond.dat >> h_bond.dat
        cat ${d%/}/hydrophobic.dat >> hydrophobic.dat
        cat ${d%/}/salt_bridges.dat >> salt_bridges.dat
        cat ${d%/}/pi_stacking.dat >> pi_stacking.dat
        cat ${d%/}/pi_cation.dat >> pi_cation.dat;
done
# INTERACTION CODES: HB=h-bond; H=hydrophobic; SB=sald bridge; pS=pi-stacking; pC=pi-cation
sed -e 's/$/ HB/' -i h_bond.dat
sed -e 's/$/ H/' -i hydrophobic.dat
sed -e 's/$/ SB/' -i salt_bridges.dat
sed -e 's/$/ pS/' -i pi_stacking.dat
sed -e 's/$/ pC/' -i pi_cation.dat
cat *dat >> all_interactions.dat
sort -o all_interactions.dat all_interactions.dat
uniq all_interactions.dat -c > unique_interactions.csv
sed -i 's/      //g' unique_interactions.csv
sed -i 's/     //g' unique_interactions.csv
sed -i 's/    //g' unique_interactions.csv
sed -i 's/   //g' unique_interactions.csv
sed -i 's/ /,/g' unique_interactions.csv
sort -t , -k 2 -g -o unique_interactions.csv unique_interactions.csv
sed -i '1 i\N,res,type' unique_interactions.csv
rm -rf model*
