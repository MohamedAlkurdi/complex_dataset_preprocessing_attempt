import os

input_dir = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\datafile1_refs_keys_content_outputs\keys_content_output.txt"

def split_datasets(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    dataset = []
    dataset_number = 0
    output_dir = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1"
    os.makedirs(output_dir, exist_ok=True)

    for line in lines:
        if '------------------------ Dataset:' in line:
            if dataset:
                save_dataset(dataset, output_dir, dataset_number)
                dataset = []
            dataset_number = extract_year(line)
        dataset.append(line)

    if dataset:
        save_dataset(dataset, output_dir, dataset_number)

def extract_year(line):
    parts = line.split()
    for part in parts:
        if part.isdigit() and len(part) == 4:
            return part
    return 'unknown_year'

def save_dataset(dataset, output_dir, dataset_number):
    output_file = os.path.join(output_dir, f'dataset_{dataset_number}.txt')
    with open(output_file, 'w') as file:
        file.writelines(dataset)

if __name__ == '__main__':
    input_file = 'large_data_file.txt'
    split_datasets(input_dir)
