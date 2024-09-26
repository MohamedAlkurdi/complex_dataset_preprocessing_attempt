import h5py
import pandas as pd

path = r"C:\Users\alkrd\Desktop\graduation_project\eSEEd_v2\data_v2.mat"

# Function to extract data and convert to DataFrame
def extract_data_to_dataframe(hdf5_file, keys):
    data_dict = {}
    with h5py.File(hdf5_file, 'r') as f:
        refs_group = f['#refs#']
        for key in keys:
            item = refs_group[key]
            if isinstance(item, h5py.Dataset):
                data_dict[key] = item[:]
    return pd.DataFrame.from_dict(data_dict, orient='index')

# Read keys from your .txt file
txt_file_path = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\refs_keys\datafile2_layer1_refs_keys.txt"
with open(txt_file_path, 'r') as file:
    keys = file.read().splitlines()

# Extract data and convert to DataFrame
df = extract_data_to_dataframe(path, keys)

# Display the DataFrame
print(df.head())
