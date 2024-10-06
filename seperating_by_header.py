import os
import re

input_file = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\datafile1_refs_keys_content_outputs\keys_content_output.txt"
output_dir = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\output_datasets_new"

def split_datasets(input_file):
    os.makedirs(output_dir, exist_ok=True)

    with open(input_file, 'r') as file:
        lines = file.readlines()

    current_dataset = []
    file_count = 0
    dataset_count = 0
    specific_number = None
    collecting_data = False

    for i, line in enumerate(lines):
        # Start a new dataset when we see "shape: (1, 6)"
        if "shape: (1, 6)" in line:
            if current_dataset:
                # Save the previous dataset
                file_count += 1
                current_file_name = f"file_{file_count}_datasets_{dataset_count}_{specific_number}.txt"
                save_dataset_to_file(current_file_name, current_dataset, output_dir)
                current_dataset = []
                dataset_count = 0  # Reset dataset count for the next file
                specific_number = None  # Reset specific number

            # Start collecting for a new dataset
            collecting_data = True

        # Extract the specific number (5th value) from the Data line
        if "Data:[[" in line and specific_number is None:
            match = re.search(r'\[\[(?:\d+\s+){4}(\d+)', line)
            if match:
                specific_number = match.group(1)

        # Check for dataset separator and increment dataset count
        if "------------------------ Dataset:" in line:
            dataset_count += 1

        # Keep adding lines until the next dataset or the end
        if collecting_data:
            current_dataset.append(line)

    # Save the last dataset if it's not saved yet
    if current_dataset:
        file_count += 1
        current_file_name = f"file_{file_count}_datasets_{dataset_count}_{specific_number}.txt"
        save_dataset_to_file(current_file_name, current_dataset, output_dir)

def save_dataset_to_file(file_name, dataset, folder):
    with open(os.path.join(folder, file_name), 'w') as f:
        f.writelines(dataset)
    print(f"Saved dataset to: {file_name}")  # Debugging statement

if __name__ == "__main__":
    split_datasets(input_file)
