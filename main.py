def split_file(file_path,number_of_files):
    lines_per_file = 45
    splitfile=None
    file_counter=1
    with open(file_path) as mainfile:
        for counter, line in enumerate(mainfile):
            if counter % lines_per_file == 0:
                if splitfile:
                    splitfile.close()
                splitfile_name = 'file{}.secret.txt'.format(file_counter)
                file_counter+=1
                splitfile =open(splitfile_name,"w")
            splitfile.write(line)
        if splitfile:
            splitfile.close()

split_file('secret.txt',3)