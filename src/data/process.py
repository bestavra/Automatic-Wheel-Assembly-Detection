#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import annotations
import os
import argparse

import torch
import pandas as pd

# Local imports
from utils import find_git_root_folder


"""process.py: Load normalized data from .csv files and save them to separate folder as .pt files."""

__author__  = "Vratislav Besta"
__group__   = "50"
__version__ = "1.0.0"
__email__   = "bestavra@fel.cvut.cz"
__date__    = "2024/01/10" 


def save_CSVs_as_tensors(src_folder: str, out_folder: str, run_in_git: bool = True) -> None:
    """Save CSV files as PyTorch tensors.
    
    Parameters
    ----------
    src_folder : str
        The path to the folder containing the CSV files.
    out_folder : str
        The path to the folder to store the PyTorch tensors.
    run_in_git : bool, optional
        Set to True if the script is run in the git repository, by default True
    """
    # If running in git, set path relative to the root of the repository
    if run_in_git:
        git_root = find_git_root_folder()
        src_folder = os.path.join(git_root, src_folder)
        out_folder = os.path.join(git_root, out_folder)

    # Create the output folder if it doesn't exist
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)

    # Iterate over all CSV files in the source folder
    for file_name in os.listdir(src_folder):
        if file_name.endswith('.csv'):
            # Construct the full file path
            file_path = os.path.join(src_folder, file_name)

            # Load the CSV file into a DataFrame
            df = pd.read_csv(file_path)

            # Convert the DataFrame into a PyTorch Tensor
            tensor = torch.tensor(df.values)

            # Save the Tensor to the output folder
            # The tensor file will have the same name as the CSV but with a .pt extension
            tensor_file_name = file_name.replace('.csv', '.pt')
            torch.save(tensor, os.path.join(out_folder, tensor_file_name))


def main() -> None:
    """The main function."""
    # Create the parser
    parser = argparse.ArgumentParser(description="Process some CSV files.")

    # Add the arguments
    parser.add_argument('normalized_data_path', type=str, help='The path to the normalized data')
    parser.add_argument('processed_data_path', type=str, help='The path to store the processed data')

    # Parse the arguments
    args = parser.parse_args()

    # Process the CSV files
    _ = save_CSVs_as_tensors(args.normalized_data_path, args.processed_data_path)

if __name__ == '__main__':
    main()