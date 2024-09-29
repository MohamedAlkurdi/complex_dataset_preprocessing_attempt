import h5py
import numpy as np

path = r"C:\Users\alkrd\Desktop\graduation_project\data.mat"
output_path = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\headers\questionnaires.txt"
dir = 'questionnaires'

def print_dataset_info(dataset, file):
    for row in dataset:
        file.write(f"[{row[0]}          {row[1]}          {row[2]}          {row[3]}       {row[4]}          {row[5]}]\n")

def dereference(references, f, file):
    dereferenced_output = [f[obj_ref] for obj_ref in references.flatten()]
    for i, ref in enumerate(dereferenced_output):
        if isinstance(ref, h5py.Dataset):
            print_dataset_info(ref, file)
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
