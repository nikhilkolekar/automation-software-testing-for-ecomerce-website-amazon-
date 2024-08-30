import os
import subprocess

# Specify the folder containing Python files
folder_path = 'C:/Users/HP/OneDrive/Desktop/Testing/all'

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Filter for Python files
python_files = [f for f in files if f.endswith('.py')]

# Run each Python file
for python_file in python_files:
    file_path = os.path.join(folder_path, python_file)
    print(f"Running {file_path}...")
    subprocess.run(['python', file_path], check=True)

print("All Python files have been executed.")
