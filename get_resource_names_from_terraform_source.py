import os
import re
import argparse

TERRAFORM_SAMPLES_DIR = "C:\\Users\\tarcher\\source\\repos\\terraform\\quickstart\\"

def list_to_string(input_list):

    # Initialize an empty string.
    return_string = ""

    # Traverse elements of list...
    for list_element in input_list:
        # Add element to string.
        return_string += list_element

    # Return string.
    return return_string

def get_file_contents(file):
    file_contents = ""

    with open(file, encoding="utf-8") as f:
        file_contents = f.readlines()

    file_contents = list_to_string(file_contents)
    return file_contents

def get_terraform_source_code(sample_dir):
    complete_source_code = ""

    full_dir = TERRAFORM_SAMPLES_DIR + sample_dir
    current_sample_source_code = ""

    # For every file in the source directory...
    for file_name in os.listdir(full_dir):
        # If the file is a Terraform file...
        if file_name.endswith('.tf'):
            # Append source code for the current directory/file
            current_sample_source_code += get_file_contents(full_dir+"\\"+file_name)

    # Update the source code for the current directory.
    complete_source_code = current_sample_source_code
    return complete_source_code

def print_resource_names(source_code):
    matches = re.findall('resource "(.*?)"', source_code)
    print(matches)

def main(sample_dir):
    parser = argparse.ArgumentParser()
    parser.add_argument("sample_dir")

    args = parser.parse_args()

    sample_code = get_terraform_source_code(args.sample_dir)
    
    print_resource_names(sample_code)

main("")
