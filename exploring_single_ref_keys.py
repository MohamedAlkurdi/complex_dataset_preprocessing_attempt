import h5py

# path = r"C:\Users\alkrd\Desktop\graduation_project\data.mat"
# txt_file_path = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\layer1_keys_output.txt"
# output_dir = r"C:\Users\alkrd\Desktop\graduation_project\datafile2_refs_keys_content_outputs\data_exploring_scripts-v1"
path = r"C:\Users\alkrd\Desktop\graduation_project\eSEEd_v2\data_v2.mat"
txt_file_path = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\datafile2_layer1_refs_keys.txt"
output_dir = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\datafile2_refs_keys_content_outputs"
batch_size = 20000

with open(txt_file_path, 'r') as file:
    keys = file.read().splitlines()

with h5py.File(path, 'r') as f:
    refs_group = f['#refs#']
    file_number = 1
    count = 0

    for i in range(0, len(keys), batch_size):
        batch_keys = keys[i:i + batch_size]
        output_file_path = f"{output_dir}/keys_content_output{file_number}.txt"
        
        with open(output_file_path, 'w') as output_file:
            for key in batch_keys:
                item = refs_group[key]
                if isinstance(item, h5py.Dataset):
                    output_file.write(f'------------------------ Dataset: {key} ------------------------\n')
                    output_file.write(f"shape: {item.shape}, dtype: {item.dtype}\n")
                    output_file.write(f"Data: {item[:]} \n")
        
        file_number += 1