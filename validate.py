import os
import sys
import re

if len(sys.argv) < 3:
    print("Invalid number of parameters.")
    print("Usage:")
    print("$ python validate.py <PATH_TO_PARENT_OF_PROJECT> <PROJECT_NAME>")
    print("Ex.")
    print("$ python validate.py /home/student/cse6250 hw4")

parent_dir_path = sys.argv[1]
project_name = sys.argv[2]

valid_project_names = ['hw4']
if project_name not in valid_project_names:
    print("Invalid project name. Valid project names are:")
    print(*valid_project_names, sep='\n')

project_directory_name_pattern = re.compile('\d{9}-[a-zA-Z0-9]+-' + project_name)

target_dir_structure_path = os.path.join('target_project_dir_structures', project_name + '.txt')
# Read in target file structure
with open(target_dir_structure_path, 'r') as dir_structure_file:
    target_dir_structure = dir_structure_file.read()

# Find project directory in parent
file_names = os.listdir(parent_dir_path)
candidate_project_dir_names = list(filter(project_directory_name_pattern.match, file_names))

# Error handling
if len(candidate_project_dir_names) > 1:
    print("Found multiple directories matching project name pattern:")
    print(*candidate_project_dir_names, sep='\n')
    exit(1)
elif len(candidate_project_dir_names) < 1:
    print("Coudn't find directory matching project name pattern:")
    print(*file_names, sep='\n')
    exit(1)

project_dir_name = candidate_project_dir_names[0]
project_dir_path = os.path.join(parent_dir_path, project_dir_name)

# Obtain project directory structure
project_files = []
for root, dirs, files in os.walk(project_dir_path, topdown=False):
    relative_root = root[root.find(project_dir_name) + len(project_dir_name) + 1:]
    for name in files:
        project_files.append(os.path.join(relative_root, name))
    for name in dirs:
        project_files.append(os.path.join(relative_root, name))

project_structure = '\n'.join(project_files)

if project_structure == target_dir_structure:
    print("Passed.")
    print(f'The structure of {project_dir_name} aligns with submission requirements.')
else:
    print('Failed.')
    print(f'Found project directory {project_dir_name} but the structure was:\n')
    print(project_structure)
    print("\nwhen it should be:\n")
    print(target_dir_structure)
    exit(1)
