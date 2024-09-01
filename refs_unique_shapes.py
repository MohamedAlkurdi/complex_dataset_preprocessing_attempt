import h5py
from collections import defaultdict


path = r"C:\Users\alkrd\Desktop\graduation_project\eSEEd_v2\data_v2.mat"
txt_file_path = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\refs_keys\datafile2_layer1_refs_keys.txt"
output_file = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\refs_keys_shape_uniqeness_statistics_datafile2.txt"

# path = r"C:\Users\alkrd\Desktop\graduation_project\data.mat"
# txt_file_path = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\refs_keys\datafile1_layer1_refs_keys.txt"
# output_file = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\refs_keys_shape_uniqeness_statistics.txt"

shape_counts = defaultdict(int)

with open(txt_file_path, 'r') as file:
    keys = file.read().splitlines()

with h5py.File(path, 'r') as f:
    refs_group = f['#refs#']

    for key in keys:
        item = refs_group[key]
        if isinstance(item, h5py.Dataset):
            shape = item.shape
            shape_counts[shape] += 1

with open(output_file, 'w') as file:
    for shape, count in shape_counts.items():
        file.write(f"Shape: {shape}, Count: {count} \n")
