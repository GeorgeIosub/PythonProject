import random
from os import path


def split_file(file_path, number_of_files):
    lines_per_file = 25
    splitfile = None
    file_counter = 1
    with open(file_path) as main_file:
        file_number_of_lines = len(main_file.readlines())
    main_file.close()
    with open(file_path) as main_file:
        if lines_per_file * number_of_files >= file_number_of_lines:
            for counter, line in enumerate(main_file):
                if counter % lines_per_file == 0:
                    if splitfile:
                        splitfile.close()
                    splitfile_name = 'file{}.secret.txt'.format(file_counter)
                    file_counter += 1
                    splitfile = open(splitfile_name, "w")
                splitfile.write(line)
            if splitfile:
                splitfile.close()
        else:
            print("The secret-file's data can't be put in {} files".format(number_of_files))
            return 0


def recompose_file(number_of_files, number_of_files_to_merge):
    file_to_merge_into_index = random.randint(1, number_of_files)
    file_to_merge_into_name = 'file{}.secret.txt'.format(file_to_merge_into_index)
    print("Main file: ", file_to_merge_into_name)
    if path.exists(file_to_merge_into_name):
        with open(file_to_merge_into_name, 'a') as file:
            for i in range(2, number_of_files_to_merge + 1):
                index = random.randint(1, number_of_files)
                file_path = 'file{}.secret.txt'.format(index)
                if path.exists(file_path):
                    print("Merged file: ", file_path)
                    with open(file_path, "r") as info_file:
                        file.write(info_file.read())
                else:
                    print("The file doesn't exist")
    else:
        print("The file doesn't exist")


split_file('secret.txt', 5)
recompose_file(5, 3)
