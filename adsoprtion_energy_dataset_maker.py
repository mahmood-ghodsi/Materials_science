#You need to make the total_e folder manually
#You need to insert the surface and molecular energy.
import os
import re
import csv
results_path = './results'
surface_e = -23905.929280
ad_sites_num = 97
molecule_energy = -40.27971791

for i in range(1,ad_sites_num):
    with open(results_path + '/ad_site_{0}.out'.format(i),'r') as f:
        h = open(results_path + '/total_e/total_{0}.txt'.format(i),'w')
        for line in f.readlines():
            if '!    total energy' in line:
                h.write(line)

energy_dict = dict()
for i in range(1,ad_sites_num):
    file_name = 'ad_site_{0}'.format(i)
    h = open(results_path + '/total_e/total_{0}.txt'.format(i),'r')
    all_lines = h.readlines()
    h.close()
    last_line = all_lines[-1]
    em_str = ""
    for m in last_line:
        if m.isdigit() or m == '.' or m == '-':
            em_str = em_str + m
    energy_dict[file_name] = float(em_str)
 
with open(results_path + '/test.csv', 'w') as f:
    for key in energy_dict.keys():
        f.write("{0},{1:.4f}\n".format(key,(energy_dict[key]-surface_e-molecule_energy)*13.6056980659))
