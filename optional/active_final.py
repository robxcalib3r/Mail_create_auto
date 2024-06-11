### Program to add those in output, which are not present in the checkFile

import re

def active_final(mainFile, checkFile, writeFile):
    main_file =  open(mainFile, 'r')
    check_from_file = open(checkFile, 'r')
    write_file = open(writeFile, 'a')
    
    
    for line in main_file:
        for chk in check_from_file:
            # if bool(re.search(chk, line)):
            #     print(line)
            #     write_file.writelines(line)
            
            print(re.search(chk, line))
        print(line)

    # for line in main_file:
    #     print(line)

def active_final_v2(mainFile, checkFile, writeFile):
    with open(mainFile, 'r') as main_file, open(checkFile, 'r') as check_from_file, open(writeFile, 'a') as write_file:
        # Read check_from_file into a set
        check_lines = set(check_from_file.read().splitlines())

        for line in main_file:
            if not any(chk in line for chk in check_lines):
                print(line)
                write_file.writelines(line)

import re

def active_final_v3(mainFile, checkFile, writeFile):
    with open(mainFile, 'r') as main_file, open(checkFile, 'r') as check_from_file, open(writeFile, 'a') as write_file:
        check_lines = set(check_from_file.read().splitlines())
        pattern = re.compile('|'.join(map(re.escape, check_lines)))

        for line in main_file:
            if pattern.search(line):
                print(line)
                write_file.writelines(line)


active_final_v2('total_active_inactive_list.txt', 'active_all.txt', 'inactive_final_output_from_all.txt')