import os
import pandas as pd

# Define the main directory containing the 49 user folders
main_dir = r"C:\Users\alkrd\Desktop\graduation_project\data_exploring_scripts-v1\grouped_video_49"

# Function to load and convert a dataset into a pandas DataFrame
def load_data(dataset, dtype):
    data = dataset['Data']  # Extracting the 'Data' part
    df = pd.DataFrame(data)
    return df.astype(dtype)

# Loop through each user's folder
for user_folder in os.listdir(main_dir):
    user_path = os.path.join(main_dir, user_folder)
    
    # Check if it's a folder
    if os.path.isdir(user_path):
        print(f"Processing data for user: {user_folder}")
        
        # Initialize an empty dictionary to hold all dataframes for this user
        user_data = {}

        # Loop through the relevant files (annotation, blinks, gaze, pupil)
        for attribute_file in ['annotation', 'blinks', 'gaze', 'pupil']:
            attribute_path = os.path.join(user_path, f"{attribute_file}.mat")

            # Load the dataset (this assumes the data has already been extracted into variables)
            dataset = load_mat_file(attribute_path)  # Custom function to load the .mat file

            # Preprocess and convert into a pandas DataFrame
            user_data[attribute_file] = load_data(dataset, dtype='uint16')  # Adjust dtype as needed

        # Combine all the attributes into a single DataFrame for the user
        combined_df = pd.concat([user_data['annotation'], user_data['blinks'], user_data['gaze'], user_data['pupil']], axis=1)

        # Save the combined DataFrame to a CSV file (or any preferred format)
        combined_df.to_csv(os.path.join(user_path, f"{user_folder}_combined.csv"), index=False)
