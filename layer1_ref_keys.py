import h5py

# path = r"C:\Users\alkrd\Desktop\graduation_project\data.mat"
path = r"C:\Users\alkrd\Desktop\graduation_project\eSEEd_v2\data_v2.mat"

# output_path = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\datafile1_layer1_refs_keys.txt"
output_path = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\datafile2_layer1_refs_keys.txt"


with h5py.File(path, 'r') as f:
    print('ROOT: ', f)
    root_keys = list(f.keys())
    print("Keys at the first layer of the .mat file structure:")
    for key in root_keys:
        print(key)

with h5py.File(path, 'r') as f:
    # Explore #refs#
    refs_group = f['#refs#']
    print("Keys in '#refs#':")
    with open(output_path, 'w') as file:
        for key in refs_group.keys():
            file.write(key+'\n')
    
    # Explore #subsystem#
    print("Explore #subsystem#")
    subsystem_group = f['#subsystem#']
    print("Keys in '#subsystem#':")
    for key in subsystem_group.keys():
        print(key)



