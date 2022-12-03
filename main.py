import errno
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
        try:
            with open(file_to_merge_into_name, 'a') as file:
                for i in range(2, number_of_files_to_merge + 1):
                    index = random.randint(1, number_of_files)
                    file_path = 'file{}.secret.txt'.format(index)
                    try:
                        print("Merged file: ", file_path)
                        with open(file_path, "r") as info_file:
                            file.write(info_file.read())
                    except IOError as err:
                        if err.errno == errno.ENOENT:
                            print(file_path, '- does not exist')
                        elif err.errno == errno.EACCES:
                            print(file_path, '- cannot be read')
                        else:
                            print(file_path, '- some other error')
        except IOError as err:
            print('error ', err.errno, ',', err.strerror)
            if err.errno == errno.EACCES:
                print(file_to_merge_into_name, 'no perms')
            elif err.errno == errno.EISDIR:
                print(file_to_merge_into_name, 'is directory')


split_file('secret.txt', 5)
recompose_file(5, 3)
