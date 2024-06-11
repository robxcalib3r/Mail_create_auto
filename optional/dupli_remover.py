import os

def remove_duplicates_from_file(input_file, output_file):
    with open(os.getcwd() + input_file, 'r') as infile:
        lines = infile.readlines()
        unique_lines = set(lines)

    with open(os.getcwd() + output_file, 'w') as outfile:
        outfile.writelines(unique_lines)

# Example usage:
remove_duplicates_from_file('/output/corrupt_all_2.txt', '/output/corrupt_all_2_final.txt')
