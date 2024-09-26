# import h5py
# from collections import defaultdict


# # path = r"C:\Users\alkrd\Desktop\graduation_project\data.mat"
# # txt_file_path = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\refs_keys\datafile1_layer1_refs_keys.txt"
# # output_file_path = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\statistics\datafile1_lowest_level_dereferences_shapes_frequencies.txt"

# path = r"C:\Users\alkrd\Desktop\graduation_project\eSEEd_v2\data_v2.mat"
# txt_file_path = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\refs_keys\datafile2_layer1_refs_keys.txt"
# output_file_path = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\statistics\datafile2_lowest_level_dereferences_shapes_frequencies.txt"



# def unique_shapes_analysis(data,f):
#     shape_counts = defaultdict(int)
#     for dataset in data:
#             if isinstance(dataset, h5py.Dataset):
#                 references = dataset[:]
#                 dereferenced_output = [f[obj_ref] for obj_ref in references.flatten()]
#                 for i, ref in enumerate(dereferenced_output):
#                     if isinstance(ref, h5py.Dataset):
#                         shape = ref.shape
#                         shape_counts[shape] += 1
#                     else:
#                         print("condition was not checked.")
#             else:
#                 print('something went wrong.')
#     with open(output_file_path, 'w') as output_file:
#         for shape, count in shape_counts.items():
#             output_file.write(f"Shape: {shape}, Count: {count} \n")

# with open(txt_file_path, 'r') as file:
#     keys = file.read().splitlines()

# with h5py.File(path, 'r') as f:
#     refs_group = f['#refs#']
#     data = []
#     with open(output_file_path, 'w') as output_file:
#         for key in keys:
#             item = refs_group[key]
#             if isinstance(item, h5py.Dataset):
#                 if item.shape == (21, 1):
#                     data.append(item)
# unique_shapes_analysis(data,f)

import h5py
from collections import defaultdict

# path = r"C:\Users\alkrd\Desktop\graduation_project\eSEEd_v2\data_v2.mat"
# txt_file_path = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\refs_keys\datafile2_layer1_refs_keys.txt"
# output_file_path = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\statistics\datafile2_lowest_level_dereferences_shapes_frequencies.txt"

path = r"C:\Users\alkrd\Desktop\graduation_project\data.mat"
txt_file_path = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\refs_keys\datafile1_layer1_refs_keys.txt"
output_file_path = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\statistics\datafile1_lowest_level_dereferences_shapes_frequencies.txt"


def unique_shapes_analysis(data, f, output_file_path):
    shape_counts = defaultdict(int)
    for dataset in data:
        if isinstance(dataset, h5py.Dataset):
            print(f"Processing dataset: {dataset.name}")
            try:
                references = dataset[:]
                dereferenced_output = []
                for obj_ref in references.flatten():
                    try:
                        dereferenced_output.append(f[obj_ref])
                    except Exception as e:
                        print(f"Error dereferencing object {obj_ref}: {e}")
                for ref in dereferenced_output:
                    if isinstance(ref, h5py.Dataset):
                        shape = ref.shape
                        shape_counts[shape] += 1
                    else:
                        print("Condition was not checked for reference:", ref)
            except Exception as e:
                print(f"Error accessing dataset: {e}")
        else:
            print('Something went wrong with dataset:', dataset)
    
    with open(output_file_path, 'w') as output_file:
        for shape, count in shape_counts.items():
            output_file.write(f"Shape: {shape}, Count: {count} \n")

with open(txt_file_path, 'r') as file:
    keys = file.read().splitlines()

with h5py.File(path, 'r') as f:
    refs_group = f['#refs#']
    data = []
    for key in keys:
        try:
            item = refs_group[key]
            if isinstance(item, h5py.Dataset):
                if item.shape == (21, 1):
                    data.append(item)
        except Exception as e:
            print(f"Error accessing key {key}: {e}")

    unique_shapes_analysis(data, f, output_file_path)
