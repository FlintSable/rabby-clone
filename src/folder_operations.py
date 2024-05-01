import os
import json

def snapshot_folder_structure(source_dir):
    # Traverse the source directory and create the folder structure
    folder_structure = {}
    for root, dirs, files in os.walk(source_dir):
        folder_structure[root] = {
            'dirs': dirs,
            'files': files
        }

    # Save the folder structure and file information as a JSON file
    with open('structure.json', 'w') as f:
        json.dump(folder_structure, f, indent=4)