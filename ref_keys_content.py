
        
# import h5py

# path = r"C:\Users\alkrd\Desktop\graduation_project\data.mat"

# def explore_group_limited(group, limit=5, level=0):
#     indent = "         " * level
#     count = 0
#     for key in group.keys():
#         if count >= limit:
#             print(f"{indent}... (output truncated, showing first {limit} keys)")
#             break
#         item = group[key]
#         if isinstance(item, h5py.Group):
#             print(f"{indent}Group: {key}")
#             explore_group_limited(item, limit, level + 1)
#         elif isinstance(item, h5py.Dataset):
#             print(f"{indent}Dataset: {key}, shape: {item.shape}, dtype: {item.dtype}")
#         count += 1

# with h5py.File(path, 'r') as f:
#     print('Exploring #refs# key with limited output:')
#     refs_group = f['#refs#']
#     explore_group_limited(refs_group)

# import h5py

# path = r"C:\Users\alkrd\Desktop\graduation_project\data.mat"
# output_path = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\output.txt"

# def explore_group_filtered(group, pattern, file, limit=30, level=0):
#     indent = "  " * level
#     count = 0
#     for key in group.keys():
#         if pattern in key:
#             if count >= limit:
#                 file.write(f"{indent}... (output truncated, showing first {limit} keys matching '{pattern}')\n")
#                 break
#             item = group[key]
#             if isinstance(item, h5py.Group):
#                 file.write(f"{indent}Group: {key}\n")
#                 explore_group_filtered(item, pattern, file, limit, level + 1)
#             elif isinstance(item, h5py.Dataset):
#                 file.write(f"{indent}Dataset: {key}, shape: {item.shape}, dtype: {item.dtype}\n")
#             count += 1
#             file.flush()  # Ensure data is written to the file

# with h5py.File(path, 'r') as f:
#     with open(output_path, 'w') as file:
#         file.write('Exploring #refs# key with filtered output:\n')
#         refs_group = f['#refs#']
#         explore_group_filtered(refs_group, pattern='a', file=file)

import h5py

# path = r"C:\Users\alkrd\Desktop\graduation_project\data.mat"
path = r"C:\Users\alkrd\Desktop\graduation_project\eSEEd_v2\data_v2.mat"
output_path = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\output.txt"

def explore_group_limited_to_file(group, file, limit=28, level=0):
    indent = "         " * level
    count = 0
    for key in group.keys():
        if count >= limit:
            file.write(f"{indent}... (output truncated, showing first {limit} keys)\n")
            break
        item = group[key]
        if isinstance(item, h5py.Group):
            file.write(f"{indent}Group: {key}\n")
            explore_group_limited_to_file(item, file, limit, level + 1)
        elif isinstance(item, h5py.Dataset):
            file.write(f"{indent}Dataset: {key}, shape: {item.shape}, dtype: {item.dtype}\n")
        count += 1
        file.flush()  # Ensure data is written to the file

with h5py.File(path, 'r') as f:
    with open(output_path, 'w') as file:
        file.write('Exploring #refs# key with limited output:\n')
        refs_group = f['#refs#']
        explore_group_limited_to_file(refs_group, file)

