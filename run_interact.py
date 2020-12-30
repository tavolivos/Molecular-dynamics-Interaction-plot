###################################
#  By: Gustavo E. Olivos-Ramirez  #
#      gustavo.olivos@upch.pe     #
#      Lima-Peru                  #
###################################

import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
from matplotlib import rc,rcParams
from pylab import *

df = pd.read_csv('unique_interactions.csv')

res = []
with open('unique_interactions.csv', 'r') as rf:
    reader = csv.reader(rf, delimiter=',')
    for row in reader:
        res.append(row[1])

y1 = []
for t,c in zip(df.type,range(len(df.type))):
    if t == 'HB':
        y1.append(df.N[c])
    else:
        y1.append(0)

outfile = open('h_bond.csv','w')
out = csv.writer(outfile)
out.writerows(zip({'res'},{'N'}))
out.writerows(zip(res[1:], y1))
outfile.close()

y2 = []
for t,c in zip(df.type,range(len(df.type))):
    if t == 'H':
        y2.append(df.N[c])
    else:
        y2.append(0)

outfile = open('hydrophobic.csv','w')
out = csv.writer(outfile)
out.writerows(zip({'res'},{'N'}))
out.writerows(zip(res[1:], y2))
outfile.close()

y3 = []
for t,c in zip(df.type,range(len(df.type))):
    if t == 'SB':
        y3.append(df.N[c])
    else:
        y3.append(0)

outfile = open('salt_bridge.csv','w')
out = csv.writer(outfile)
out.writerows(zip({'res'},{'N'}))
out.writerows(zip(res[1:], y3))
outfile.close()

y4 = []
for t,c in zip(df.type,range(len(df.type))):
    if t == 'pS':
        y4.append(df.N[c])
    else:
        y4.append(0)

outfile = open('pi_stacking.csv','w')
out = csv.writer(outfile)
out.writerows(zip({'res'},{'N'}))
out.writerows(zip(res[1:], y4))
outfile.close()

y5 = []
for t,c in zip(df.type,range(len(df.type))):
    if t == 'pC':
        y5.append(df.N[c])
    else:
        y5.append(0)

outfile = open('pi_cation.csv','w')
out = csv.writer(outfile)
out.writerows(zip({'res'},{'N'}))
out.writerows(zip(res[1:], y5))
outfile.close()

#H-bond
h_bond = "h_bond.csv"
h_bond_u = "h_bond_u.csv"

df = pd.read_csv(h_bond, sep=",")
df.drop_duplicates(subset=None, inplace=True)
df.to_csv(h_bond_u, index=False)

df = pd.read_csv("h_bond_u.csv")

df = df.sort_values(by='N', ascending=False)
df = df.drop_duplicates(subset='res', keep="first")
df = df.sort_values(by='res', ascending=False)
df.to_csv(h_bond_u, index=False)

os.remove("h_bond.csv")
os.rename(r'h_bond_u.csv',r'h_bond.csv')

#Hydrophobic
h_bond = "hydrophobic.csv"
h_bond_u = "hydrophobic_u.csv"

df = pd.read_csv(h_bond, sep=",")
df.drop_duplicates(subset=None, inplace=True)
df.to_csv(h_bond_u, index=False)

df = pd.read_csv("hydrophobic_u.csv")

df = df.sort_values(by='N', ascending=False)
df = df.drop_duplicates(subset='res', keep="first")
df = df.sort_values(by='res', ascending=False)
df.to_csv(h_bond_u, index=False)

os.remove("hydrophobic.csv")
os.rename(r'hydrophobic_u.csv',r'hydrophobic.csv')

#Salt-bridge
h_bond = "salt_bridge.csv"
h_bond_u = "salt_bridge_u.csv"

df = pd.read_csv(h_bond, sep=",")
df.drop_duplicates(subset=None, inplace=True)
df.to_csv(h_bond_u, index=False)

df = pd.read_csv("salt_bridge_u.csv")

df = df.sort_values(by='N', ascending=False)
df = df.drop_duplicates(subset='res', keep="first")
df = df.sort_values(by='res', ascending=False)
df.to_csv(h_bond_u, index=False)

os.remove("salt_bridge.csv")
os.rename(r'salt_bridge_u.csv',r'salt_bridge.csv')

#pi-Cation
h_bond = "pi_cation.csv"
h_bond_u = "pi_cation_u.csv"

df = pd.read_csv(h_bond, sep=",")
df.drop_duplicates(subset=None, inplace=True)
df.to_csv(h_bond_u, index=False)

df = pd.read_csv("pi_cation_u.csv")

df = df.sort_values(by='N', ascending=False)
df = df.drop_duplicates(subset='res', keep="first")
df = df.sort_values(by='res', ascending=False)
df.to_csv(h_bond_u, index=False)

os.remove("pi_cation.csv")
os.rename(r'pi_cation_u.csv',r'pi_cation.csv')

#pi-Stacking
h_bond = "pi_stacking.csv"
h_bond_u = "pi_stacking_u.csv"

df = pd.read_csv(h_bond, sep=",")
df.drop_duplicates(subset=None, inplace=True)
df.to_csv(h_bond_u, index=False)

df = pd.read_csv("pi_stacking_u.csv")

df = df.sort_values(by='N', ascending=False)
df = df.drop_duplicates(subset='res', keep="first")
df = df.sort_values(by='res', ascending=False)
df.to_csv(h_bond_u, index=False)

os.remove("pi_stacking.csv")
os.rename(r'pi_stacking_u.csv',r'pi_stacking.csv')

#H-BOND
f = open('h_bond.csv','r')
filedata = f.read()
f.close()

newdata = filedata.replace("-",",")

f = open('h_bond.csv','w')
f.write(newdata)
f.close()

with open('h_bond.csv') as fin:
    lines = fin.readlines()
lines[0] = lines[0].replace('res,N', 'num,res,N')

with open('h_bond.csv', 'w') as fout:
    for line in lines:
        fout.write(line)

df = pd.read_csv('h_bond.csv')
final_df = df.sort_values(by=['num'], ascending=True)
final_df.to_csv('h_bond.csv', index=False)

with open('h_bond.csv') as f:
    reader = csv.reader(f)
    with open('out.csv', 'w') as g:
        writer = csv.writer(g)
        for row in reader:
            new_row = [' '.join([row[0], row[1]])] + row[2:]
            writer.writerow(new_row)

os.remove("h_bond.csv")

f = open('out.csv','r')
filedata = f.read()
f.close()
newdata = filedata.replace(" ","-")
f = open('out.csv','w')
f.write(newdata)
f.close()

with open('out.csv') as fin:
    lines = fin.readlines()
lines[0] = lines[0].replace('num-res,N', 'res,N')

with open('h_bond.csv', 'w') as fout:
    for line in lines:
        fout.write(line)

os.remove("out.csv")

#Hydrophobic
f = open('hydrophobic.csv','r')
filedata = f.read()
f.close()

newdata = filedata.replace("-",",")

f = open('hydrophobic.csv','w')
f.write(newdata)
f.close()

with open('hydrophobic.csv') as fin:
    lines = fin.readlines()
lines[0] = lines[0].replace('res,N', 'num,res,N')

with open('hydrophobic.csv', 'w') as fout:
    for line in lines:
        fout.write(line)

df = pd.read_csv('hydrophobic.csv')
final_df = df.sort_values(by=['num'], ascending=True)
final_df.to_csv('hydrophobic.csv', index=False)

with open('hydrophobic.csv') as f:
    reader = csv.reader(f)
    with open('out.csv', 'w') as g:
        writer = csv.writer(g)
        for row in reader:
            new_row = [' '.join([row[0], row[1]])] + row[2:]
            writer.writerow(new_row)

os.remove("hydrophobic.csv")

f = open('out.csv','r')
filedata = f.read()
f.close()
newdata = filedata.replace(" ","-")
f = open('out.csv','w')
f.write(newdata)
f.close()

with open('out.csv') as fin:
    lines = fin.readlines()
lines[0] = lines[0].replace('num-res,N', 'res,N')

with open('hydrophobic.csv', 'w') as fout:
    for line in lines:
        fout.write(line)

os.remove("out.csv")

#salt_bridge
f = open('salt_bridge.csv','r')
filedata = f.read()
f.close()

newdata = filedata.replace("-",",")

f = open('salt_bridge.csv','w')
f.write(newdata)
f.close()

with open('salt_bridge.csv') as fin:
    lines = fin.readlines()
lines[0] = lines[0].replace('res,N', 'num,res,N')

with open('salt_bridge.csv', 'w') as fout:
    for line in lines:
        fout.write(line)

df = pd.read_csv('salt_bridge.csv')
final_df = df.sort_values(by=['num'], ascending=True)
final_df.to_csv('salt_bridge.csv', index=False)

with open('salt_bridge.csv') as f:
    reader = csv.reader(f)
    with open('out.csv', 'w') as g:
        writer = csv.writer(g)
        for row in reader:
            new_row = [' '.join([row[0], row[1]])] + row[2:]
            writer.writerow(new_row)

os.remove("salt_bridge.csv")

f = open('out.csv','r')
filedata = f.read()
f.close()
newdata = filedata.replace(" ","-")
f = open('out.csv','w')
f.write(newdata)
f.close()

with open('out.csv') as fin:
    lines = fin.readlines()
lines[0] = lines[0].replace('num-res,N', 'res,N')

with open('salt_bridge.csv', 'w') as fout:
    for line in lines:
        fout.write(line)

os.remove("out.csv")

#pi_stacking
f = open('pi_stacking.csv','r')
filedata = f.read()
f.close()

newdata = filedata.replace("-",",")

f = open('pi_stacking.csv','w')
f.write(newdata)
f.close()

with open('pi_stacking.csv') as fin:
    lines = fin.readlines()
lines[0] = lines[0].replace('res,N', 'num,res,N')

with open('pi_stacking.csv', 'w') as fout:
    for line in lines:
        fout.write(line)

df = pd.read_csv('pi_stacking.csv')
final_df = df.sort_values(by=['num'], ascending=True)
final_df.to_csv('pi_stacking.csv', index=False)

with open('pi_stacking.csv') as f:
    reader = csv.reader(f)
    with open('out.csv', 'w') as g:
        writer = csv.writer(g)
        for row in reader:
            new_row = [' '.join([row[0], row[1]])] + row[2:]
            writer.writerow(new_row)

os.remove("pi_stacking.csv")

f = open('out.csv','r')
filedata = f.read()
f.close()
newdata = filedata.replace(" ","-")
f = open('out.csv','w')
f.write(newdata)
f.close()

with open('out.csv') as fin:
    lines = fin.readlines()
lines[0] = lines[0].replace('num-res,N', 'res,N')

with open('pi_stacking.csv', 'w') as fout:
    for line in lines:
        fout.write(line)

os.remove("out.csv")

#pi_cation
f = open('pi_cation.csv','r')
filedata = f.read()
f.close()

newdata = filedata.replace("-",",")

f = open('pi_cation.csv','w')
f.write(newdata)
f.close()

with open('pi_cation.csv') as fin:
    lines = fin.readlines()
lines[0] = lines[0].replace('res,N', 'num,res,N')

with open('pi_cation.csv', 'w') as fout:
    for line in lines:
        fout.write(line)

df = pd.read_csv('pi_cation.csv')
final_df = df.sort_values(by=['num'], ascending=True)
final_df.to_csv('pi_cation.csv', index=False)

with open('pi_cation.csv') as f:
    reader = csv.reader(f)
    with open('out.csv', 'w') as g:
        writer = csv.writer(g)
        for row in reader:
            new_row = [' '.join([row[0], row[1]])] + row[2:]
            writer.writerow(new_row)

os.remove("pi_cation.csv")

f = open('out.csv','r')
filedata = f.read()
f.close()
newdata = filedata.replace(" ","-")
f = open('out.csv','w')
f.write(newdata)
f.close()

with open('out.csv') as fin:
    lines = fin.readlines()
lines[0] = lines[0].replace('num-res,N', 'res,N')

with open('pi_cation.csv', 'w') as fout:
    for line in lines:
        fout.write(line)

os.remove("out.csv")

import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
from matplotlib import rc,rcParams
from pylab import *

df = pd.read_csv('h_bond.csv')
x1 = df.res
y1 = df.N

df = pd.read_csv('hydrophobic.csv')
x2 = df.res
y2 = df.N

df = pd.read_csv('salt_bridge.csv')
x3 = df.res
y3 = df.N

df = pd.read_csv('pi_stacking.csv')
x4 = df.res
y4 = df.N

df = pd.read_csv('pi_cation.csv')
x5 = df.res
y5 = df.N

font = {'family' : 'DejaVu Sans',
        'weight' : 'bold',
        'size'   : 10}
plt.rc('font', **font)
rc('axes', linewidth=2)

fig = plt.figure(figsize=(6.5,3))
ax = gca()

fig.subplots_adjust(bottom=0.35, left=0.12)

rc('axes', linewidth=2)
plt.bar(x1, y1, label='H-bond')
plt.bar(x2, y2, bottom=y1, label='Hydrophobic')
plt.bar(x3, y3, bottom=y1+y2, label='Salt-bridge')
plt.bar(x4, y4, bottom=y1+y2+y3, label='pi-Stacking')
plt.bar(x5, y5, bottom=y1+y2+y3+y4, label='pi-Cation')

ylabel(r'Number of interactions' + '\n' +'(40 ns)', fontsize=10,weight='bold')
xlabel(r'Residues', fontsize=10, weight='bold')

ax.xaxis.set_tick_params(labelsize=8)
ax.yaxis.set_tick_params(labelsize=9)
ax.set_ylim(0,800)

plt.xticks(rotation=90)
plt.legend(fancybox=True, framealpha=0, prop={'size': 8},loc=0)

fig.savefig("interac.png", format='png', dpi=350, transparent=True)
