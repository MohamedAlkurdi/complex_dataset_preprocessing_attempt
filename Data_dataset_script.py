# 

import h5py
import numpy as np

path = r"C:\Users\alkrd\Desktop\graduation_project\data.mat"
output_path = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\Data_dataset_content.txt"

def dereference(references, f, file):
    dereferenced_output = [f[obj_ref] for obj_ref in references.flatten()]
    for i, ref in enumerate(dereferenced_output):
        file.write(f"Dereferenced data {i} type: {type(ref)}\n")
        if isinstance(ref, h5py.Dataset):
            file.write(f"Dereferenced data {i} as below:\n")
            print_dataset_info(ref, file)
        elif isinstance(ref, h5py.Group):
            file.write(f"Dereferenced data {i} is a group with keys: {list(ref.keys())}\n")
            process_group(ref, f, file)
        else:
            file.write(f"Dereferenced data {i} is of type {type(ref)} and cannot be processed directly.\n")

def print_dataset_info(dataset, file):
    file.write(f"Shape: {dataset.shape}\n")
    file.write(f"Data type: {dataset.dtype}\n")
    file.write(f"Data: {dataset[:]}\n")

def process_group(group, f, file):
    file.write("------------------- group processing begins here -------------------\n")
    for key in group.keys():
        file.write(f"Group key: {key}\n")
        if isinstance(group[key], h5py.Dataset):
            file.write(f"{key} is a dataset.\n")
            print_dataset_info(group[key], file)
            references = group[key][:]
            dereference(references, f, file)
        elif isinstance(group[key], h5py.Group):
            file.write(f"{key} is a group.\n")
            process_group(group[key], f, file)

with h5py.File(path, 'r') as f, open(output_path, 'w') as file:
    file.write('ROOT: ' + str(f) + '\n')
    data_group = f['Data']
    for key in data_group.keys():
        file.write(f"key: {key}\n")
        if isinstance(data_group[key], h5py.Dataset):
            file.write(f"{key} is a dataset.\n")
            dataset = data_group[key]
            print_dataset_info(dataset, file)
            references = dataset[:]
            file.write(f"References: {references}\n")
            dereference(references, f, file)
            file.write('-----------------\n')
