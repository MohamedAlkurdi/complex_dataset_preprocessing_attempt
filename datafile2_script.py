import h5py
import numpy as np

path = r"C:\Users\alkrd\Desktop\graduation_project\eSEEd_v2\data_v2.mat"

def dereference(references, f):
    dereferenced_output = [f[obj_ref] for obj_ref in references.flatten()]
    for i, ref in enumerate(dereferenced_output):
        print(f"Dereferenced data {i} type:", type(ref))
        if isinstance(ref, h5py.Dataset):
            print(f"Dereferenced data {i} as below:")
            print_dataset_info(ref)
        elif isinstance(ref, h5py.Group):
            print(f"Dereferenced data {i} is a group with keys:", list(ref.keys()))
            process_group(ref, f)
        else:
            print(f"Dereferenced data {i} is of type {type(ref)} and cannot be processed directly.")

def print_dataset_info(dataset):
    print("Shape:", dataset.shape)
    print("Data type:", dataset.dtype)
    print("Sample data:", dataset[:1])

def process_group(group, f):
    print("------------------- group processing begins here -------------------")
    for key in group.keys():
        print(f"Group key: {key}")
        if isinstance(group[key], h5py.Dataset):
            print(f"{key} is a dataset.")
            print_dataset_info(group[key])
            references = group[key][:]
            dereference(references, f)
        elif isinstance(group[key], h5py.Group):
            print(f"{key} is a group.")
            process_group(group[key], f)

with h5py.File(path, 'r') as f:
    print('ROOT: ', f)
    data_group = f['Data']
    for key in data_group.keys():
        print("key:", key)
        if isinstance(data_group[key], h5py.Dataset):
            print(key + " is a dataset.")
            dataset = data_group[key]
            print_dataset_info(dataset)
            references = dataset[0:1]
            print("References:", references)
            dereference(references, f)
            print('-----------------')
