import dicom2nifti
import os

dcm_path = 'data/dcm/'  # Update with your actual path
temp_CT_dir = 'data/nifti/'  # Update with your actual path

if not os.path.exists(temp_CT_dir):
    os.makedirs(temp_CT_dir)

dicom2nifti.convert_directory(dcm_path, temp_CT_dir, compression=True)
