import h5py
import numpy as np

path = r"C:\Users\alkrd\Desktop\graduation_project\data.mat"
output_path = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\headers\video.txt"
dir = 'video'

def print_dataset_info(dataset, file):
    for row in dataset:
        file.write(f"{row}\n")
        return
        # file.write(f"[{row[0]}          {row[1]}          {row[2]}          {row[3]}       {row[4]}          {row[5]}]\n")

def process_group(group, f, file):
    # file.write("------------------- group processing begins here -------------------\n")
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

def dereference(references, f, file):
    dereferenced_output = [f[obj_ref] for obj_ref in references.flatten()]
    for i, ref in enumerate(dereferenced_output):
        if isinstance(ref, h5py.Dataset):
            # file.write(f"Dereferenced data {i} as below:\n")
            print_dataset_info(ref, file)
        elif isinstance(ref, h5py.Group):
            file.write('------------------------------------------------------------------------------------------------\n')
            file.write(f"Dereferenced data {i} is a group with keys: {list(ref.keys())}\n")
            process_group(ref, f, file)
        else:
            file.write(f"Dereferenced data {i} is of type {type(ref)} and cannot be processed directly.\n")

with h5py.File(path, 'r') as f, open(output_path, 'w') as file:
    data_group = f['Data']
    if isinstance(data_group[dir], h5py.Dataset):
        dataset = data_group[dir]
        references = dataset[:]
        dereference(references, f, file)
    else:
        print('null.')
