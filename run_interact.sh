###################################
#  By: Gustavo E. Olivos-Ramirez  #
#      gustavo.olivos@upch.pe     #
#      Lima-Peru                  #
###################################

ligand_code=LIG
pdb=all.pdb
i=1
while read line; do
	echo "$i"
	echo "${line}" >> model_${i}.pdb
	[[ ${line[0]} == ENDMDL ]] && ((i++))
done < $pdb
for file in model_*; do
	sed -i '1,1d' ${file}
	mkdir ${file%.pdb} && mv ${file} ${file%.pdb};
done
n=0
for d in model_*; do
	cd ${d}
	plip -f model_* -t -q -s
	((n++))
	echo $n " plip done!"
	cd ../;
done
rm */*proton*
rm */*fixed*

k=1
for d in */; do
	echo "$k"
        cd ${d}
        sed -n -e '/('$ligand_code') - SMALLMOLECULE/,/SMALLMOLECULE/p' *.txt > all_interact.dat
	echo "**" >> all_interact.dat
        sed -i -z 's/+//g; s/-//g; s/=//g; s/|//g; s/*\*\n/\n/g' all_interact.dat
	awk '{print $1,$2}' all_interact.dat > res_interact.dat
	sed -i '/^ $/d' res_interact.dat
#Hydrophobic
        sed -n -e '/Hydrophobic Interactions/,/*/p' res_interact.dat > hydrophobic.dat
        sed -i 's/ /-/g' hydrophobic.dat
	sed -i '/*/d' hydrophobic.dat
        sed -i '1d' hydrophobic.dat
#H-bond
    	sed -n -e '/Hydrogen Bonds/,/*/p' res_interact.dat > h_bond.dat
	sed -i 's/ /-/g' h_bond.dat
	sed -i '/*/d' h_bond.dat
        sed -i '1d' h_bond.dat 
#Salt-bridges
        sed -n -e '/Salt Bridges/,/*/p' res_interact.dat > salt_bridges.dat
	sed -i 's/ /-/g' salt_bridges.dat
	sed -i '/*/d' salt_bridges.dat
        sed -i '1d' salt_bridges.dat
#pi-Stacking
        sed -n -e '/piStacking/,/*/p' res_interact.dat > pi_stacking.dat
	sed -i 's/ /-/g' pi_stacking.dat
	sed -i '/*/d' pi_stacking.dat
        sed -i '1d' pi_stacking.dat
#pi-Cation
        sed -n -e '/piCation/,/*/p' res_interact.dat > pi_cation.dat
	sed -i 's/ /-/g' pi_cation.dat
	sed -i '/*/d' pi_cation.dat
        sed -i '1d' pi_cation.dat
        cd ../
	((k++));
done
cat */h_bond.dat >> h_bond.dat
cat */hydrophobic.dat >> hydrophobic.dat
cat */salt_bridges.dat >> salt_bridges.dat
cat */pi_stacking.dat >> pi_stacking.dat
cat */pi_cation.dat >> pi_cation.dat
# INTERACTION CODES: HB=h-bond; H=hydrophobic; SB=sald bridge; pS=pi-stacking; pC=pi-cation
sed -e 's/$/ HB/' -i h_bond.dat
sed -e 's/$/ H/' -i hydrophobic.dat
sed -e 's/$/ SB/' -i salt_bridges.dat
sed -e 's/$/ pS/' -i pi_stacking.dat
sed -e 's/$/ pC/' -i pi_cation.dat
cat *dat >> all_interactions.dat
sort -o all_interactions.dat all_interactions.dat
uniq all_interactions.dat -c > unique.csv
sed -i 's/          //g' unique.csv
sed -i 's/         //g' unique.csv
sed -i 's/        //g' unique.csv
sed -i 's/       //g' unique.csv
sed -i 's/      //g' unique.csv
sed -i 's/     //g' unique.csv
sed -i 's/    //g' unique.csv
sed -i 's/   //g' unique.csv
sed -i 's/  //g' unique.csv
sed -i 's/ /,/g' unique.csv
sort -t , -k 2 -g -o unique.csv unique.csv
sed -i '1 i\N,res,type' unique.csv
mkdir plip_results
mv model_* plip_results
