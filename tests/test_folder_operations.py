import os
import json
import shutil
import unittest
from src.folder_operations import snapshot_folder_structure

class TestSnapshotFolderStructure(unittest.TestCase):
    def setUp(self):
        # Create a temporary source directory for testing
        self.source_dir = 'test_source_dir'
        os.makedirs(os.path.join(self.source_dir, 'subdir1'), exist_ok=True)
        os.makedirs(os.path.join(self.source_dir, 'subdir2'), exist_ok=True)
        with open(os.path.join(self.source_dir, 'file1.txt'), 'w') as f:
            f.write('File 1 content')
        with open(os.path.join(self.source_dir, 'subdir1', 'file2.txt'), 'w') as f:
            f.write('File 2 content')

    def tearDown(self):
        # Clean up the temporary source directory and JSON file after testing
        shutil.rmtree(self.source_dir)
        if os.path.exists('structure.json'):
            os.remove('structure.json')

    def compare_structures(self, structure1, structure2):
        if isinstance(structure1, dict) and isinstance(structure2, dict):
            self.assertEqual(set(structure1.keys()), set(structure2.keys()))
            for key in structure1:
                if key == 'dirs':
                    self.assertCountEqual(structure1[key], structure2[key])
                else:
                    self.compare_structures(structure1[key], structure2[key])
        else:
            self.assertEqual(structure1, structure2)

    def test_snapshot_folder_structure(self):
        # Test the create_folder_structure function
        snapshot_folder_structure(self.source_dir)

        # Check if the JSON file is created
        self.assertTrue(os.path.exists('structure.json'))

        # Check the content of the JSON file
        with open('structure.json', 'r') as f:
            structure = json.load(f)

        expected_structure = {
            self.source_dir: {
                'dirs': ['subdir1', 'subdir2'],
                'files': ['file1.txt']
            },
            os.path.join(self.source_dir, 'subdir1'): {
                'dirs': [],
                'files': ['file2.txt']
            },
            os.path.join(self.source_dir, 'subdir2'): {
                'dirs': [],
                'files': []
            }
        }
        self.compare_structures(structure, expected_structure)

if __name__ == '__main__':
    unittest.main()