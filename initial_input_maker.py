#this range is basically the number of your files for example when I have 5 inputs starting from ad_site_1 to ad_site_5 the range will be range(1,6)
#You need to have two files: 1) the file where you get your desired coordinates from, 2) the file where you get initial tags of calculation from
file_numbers = 97
for i in range(1,file_numbers):
    #opening the file which you have the right coordinates in
    with open('./ad_site_{0}.in'.format(i),'r') as f:
        mid_all_lines = f.readlines()
        mid_lines = mid_all_lines[19:85]
    f.close()
    #Opening the reference file which you want to copy your parameters from
    with open('./RP-5050-N2.in','r') as f:
        main_all_lines = f.readlines()
        top_lines = main_all_lines[0:53]
        bot_lines = main_all_lines[120:] 
    f.close()
    with open('./ad_site_{0}.in'.format(i),'w') as f:
        for line in top_lines:
            f.write(line)
        for line in mid_lines:
            f.write(line)
        for line in bot_lines:
            f.write(line)
    f.close()
    with open('./ad_site_{0}.in'.format(i),'r') as f:
        text = f.read()
    text = text.replace('tmp1','tmp{0}'.format(i))  
    with open('./ad_site_{0}.in'.format(i),'w') as f:
        f.write(text)
    f.close()
