import os
import re

# Paths
original_txt_folder = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\output_datasets_new"
output_folder_base = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\grouped_video_49"

# Define the year-like number ranges for each category
annotation_ranges = [(31 + i * 40, 40 + i * 40) for i in range(49)]
blinks_ranges = [(21 + i * 40, 30 + i * 40) for i in range(49)]
gaze_ranges = [(1 + i * 40, 10 + i * 40) for i in range(49)]
pupil_ranges = [(11 + i * 40, 20 + i * 40) for i in range(49)]

# Regular expression to extract the year-like number from the filename
year_like_re = re.compile(r'file_\d+_datasets_\d+_(\d+)\.txt')

# Function to get files in the specified range and sort them by year_like_number
def get_files_in_range(folder, file_list, start, end):
    matched_files = []
    
    for file_name in file_list:
        match = year_like_re.search(file_name)
        if match:
            year_like_number = int(match.group(1))
            if start <= year_like_number <= end:
                matched_files.append((year_like_number, file_name))  # Store tuple (year_like_number, file_name)

    # Sort the matched files by year_like_number before returning the file names
    matched_files.sort(key=lambda x: x[0])
    return [file_name for _, file_name in matched_files]

# Function to merge files into a single output file
def merge_files(files, output_file, folder):
    with open(output_file, 'w') as out_file:
        for file_name in files:
            with open(os.path.join(folder, file_name), 'r') as f:
                out_file.write(f.read())
                out_file.write("\n")  # Optional: add separator between file contents
    print(f"Saved {output_file}")

# Main function to create new folders and organize the files
def organize_files():
    os.makedirs(output_folder_base, exist_ok=True)

    # Get all files from the original txt folder
    original_files = [f for f in os.listdir(original_txt_folder) if f.endswith('.txt')]

    for i in range(49):
        # Create new folder
        new_folder = os.path.join(output_folder_base, f'User_{i+1}')
        os.makedirs(new_folder, exist_ok=True)

        # Get files for each category and ensure they are sorted
        annotation_files = get_files_in_range(original_txt_folder, original_files, annotation_ranges[i][0], annotation_ranges[i][1])
        blinks_files = get_files_in_range(original_txt_folder, original_files, blinks_ranges[i][0], blinks_ranges[i][1])
        gaze_files = get_files_in_range(original_txt_folder, original_files, gaze_ranges[i][0], gaze_ranges[i][1])
        pupil_files = get_files_in_range(original_txt_folder, original_files, pupil_ranges[i][0], pupil_ranges[i][1])

        # Merge and save each category into its respective file
        merge_files(annotation_files, os.path.join(new_folder, f'annotation_group_in_{annotation_ranges[i][0]}_{annotation_ranges[i][1]}_range.txt'), original_txt_folder)
        merge_files(blinks_files, os.path.join(new_folder, f'blinks_group_in_{blinks_ranges[i][0]}_{blinks_ranges[i][1]}_range.txt'), original_txt_folder)
        merge_files(gaze_files, os.path.join(new_folder, f'gaze_group_in_{gaze_ranges[i][0]}_{gaze_ranges[i][1]}_range.txt'), original_txt_folder)
        merge_files(pupil_files, os.path.join(new_folder, f'pupil_group_in_{pupil_ranges[i][0]}_{pupil_ranges[i][1]}_range.txt'), original_txt_folder)

if __name__ == "__main__":
    organize_files()
