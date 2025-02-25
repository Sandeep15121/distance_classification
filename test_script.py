# test_script.py
import os

# Check if the dataset file exists
dataset_path = 'dataset.csv'
if os.path.exists(dataset_path):
    print(f"Dataset file '{dataset_path}' found.")
else:
    print(f"Dataset file '{dataset_path}' not found.")

# Check if the distance_classification.py script exists
script_path = 'distance_classification.py'
if os.path.exists(script_path):
    print(f"Script file '{script_path}' found.")
else:
    print(f"Script file '{script_path}' not found.")