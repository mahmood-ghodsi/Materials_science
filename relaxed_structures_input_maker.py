results_path = '/Users/parastooagharezaei/Downloads/test1/not_fixed_positions/results'
file_num = 97
for i in range(1,file_number):
    with open(results_path + '/ad_site_{0}.out'.format(i),'r') as infile, open(results_path + '/final_coordinates/RP_ad_site_{0}.in'.format(i), 'w') as outfile:
        copy = False
        for line in infile:
            if line.strip() == "Begin final coordinates":
                copy = True
                continue
            elif line.strip() == "End final coordinates":
                copy = False
                continue
            elif copy:
                outfile.write(line)

for i in range(1,file_number):
    #opening the file which you have the right coordinates in
    with open(results_path + '/final_coordinates/RP_ad_site_{0}.in'.format(i),'r') as f:
        mid_all_lines = f.readlines()
        mid_lines = mid_all_lines[2:]
    f.close()
    #Opening the reference file which you want to copy your parameters from
    with open('/Users/parastooagharezaei/Downloads/test1/not_fixed_positions/RP-5050-N2.in','r') as f:
        main_all_lines = f.readlines()
        top_lines = main_all_lines[0:53]
        bot_lines = main_all_lines[120:]
    f.close()
    with open(results_path + '/final_RP_inputs/RP_ad_site_{0}.in'.format(i),'w') as f:
        for line in top_lines:
            f.write(line)
        for line in mid_lines:
            f.write(line)
        for line in bot_lines:
            f.write(line)
    f.close()

