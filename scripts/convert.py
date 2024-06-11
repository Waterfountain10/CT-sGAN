import dicom2nifti
import os

dcm_path = 'data/dcm/'  # Path where the DICOM files are located
temp_CT_dir = 'data/nifti/'  # Path where you want to store the NIFTI files

if not os.path.exists(temp_CT_dir):
    os.makedirs(temp_CT_dir)

dicom2nifti.convert_directory(dcm_path, temp_CT_dir, compression=True)
