import h5py

path = r"C:\Users\alkrd\Desktop\graduation_project\data.mat"
txt_file_path = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\refs_keys\datafile1_layer1_refs_keys.txt"
output_file_path = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\false\lowest_level_dereferences.txt"

def dereference(references, f, file):
    dereferenced_output = [f[obj_ref] for obj_ref in references.flatten()]
    for i, ref in enumerate(dereferenced_output):
        file.write(f"Dereferenced data {i} type: {type(ref)}\n")
        if isinstance(ref, h5py.Dataset):
            file.write(f"Shape: {ref.shape}\n")
            file.write(f"Data type: {ref.dtype}\n")
            file.write(f"Data: {ref[:]}\n")
        else:
            file.write(f"Dereferenced data {i} is of type {type(ref)} and cannot be processed directly.\n")

with open(txt_file_path, 'r') as file:
    keys = file.read().splitlines()

with h5py.File(path, 'r') as f:
    refs_group = f['#refs#']

    with open(output_file_path, 'w') as output_file:
        for key in keys:
            item = refs_group[key]
            if isinstance(item, h5py.Dataset):
                if item.shape == (21, 1):
                    print('references detected using shape.')
                    output_file.write(f'------------------------ Dataset: {key} ------------------------\n')
                    output_file.write(f"shape: {item.shape}, dtype: {item.dtype}\n")
                    output_file.write(f"Data: {item[:]} \n")
                    dereference(item[:], f, output_file)
