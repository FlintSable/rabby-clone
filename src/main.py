import argparse
from folder_operations import create_folder_structure
from file_operations import copy_files

def parse_arguments():
    parser = argparse.ArgumentParser(description='Rabby Clone - Mac to Mac Migration Utility')
    parser.add_argument('--source', help='Path to the source directory')
    parser.add_argument('--target', help='Path to the target directory')
    parser.add_argument('--mode', choices=['live', 'archive'], help='Copying mode: live or archive')
    return parser.parse_args()

def main():
    args = parse_arguments()
    create_folder_structure(args.source, args.target)
    copy_files(args.source, args.target, args.mode)

if __name__ == '__main__':
    main()