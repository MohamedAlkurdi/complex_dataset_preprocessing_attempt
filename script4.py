import h5py
import numpy as np

path = r"C:\Users\alkrd\Desktop\graduation_project\data.mat"

def print_dataset_info(dataset):
    print("Shape:", dataset.shape)
    print("Data type:", dataset.dtype)
    print("Sample data:", dataset[:5])  # Print first 5 elements as a sample

with h5py.File(path, 'r') as f:
    data_group = f['Data']
    
    for key in data_group.keys():
        print("key:", key)

        if isinstance(data_group[key], h5py.Dataset):
            print(key + " is a dataset.")
            dataset = data_group[key]
            print_dataset_info(dataset)
            
            references = dataset[3:6]
            print("References:", references)
            
            dereferenced_output = [f[obj_ref] for obj_ref in references.flatten()]
            for i, ref in enumerate(dereferenced_output):
                print(f"Dereferenced data {i} type:", type(ref))
                if isinstance(ref, h5py.Dataset):
                    print(f"Dereferenced data {i}:")
                    print_dataset_info(ref)
                elif isinstance(ref, h5py.Group):
                    print(f"Dereferenced data {i} is a group with keys:", list(ref.keys()))
                else:
                    print(f"Dereferenced data {i} is of type {type(ref)} and cannot be processed directly.")
            print('-----------------')
