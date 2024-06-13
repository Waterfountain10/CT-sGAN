import dicom2nifti
import os
import logging
from tqdm import tqdm

# Set up logging for the conversion process
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='conversion.log', filemode='w')

dcm_path = '../data/dcm'
nifti_path = '../data/nifti'
processed_log = 'processed_files.log'

if not os.path.exists(nifti_path):
    os.makedirs(nifti_path)

# Load the list of already processed files
if os.path.exists(processed_log):
    with open(processed_log, 'r') as f:
        processed_files = set(line.strip() for line in f)
else:
    processed_files = set()

# Function to convert a batch of DICOM files to NIFTI
def convert_batch(dcm_files, nifti_dir):
    for dcm_file in tqdm(dcm_files, desc="Converting batch"):
        if dcm_file in processed_files:
            continue  # Skip already processed files

        try:
            dicom2nifti.convert_directory(os.path.dirname(dcm_file), nifti_dir, compression=True)
            with open(processed_log, 'a') as f:
                f.write(dcm_file + '\n')  # Log the successfully processed file
        except Exception as e:
            logging.error(f"Failed to convert {dcm_file}: {e}")

# Function to convert DICOM to NIFTI in batches
def convert_dicom_to_nifti(dcm_dir, nifti_dir, batch_size=100):
    logging.info(f"Starting conversion of DICOM files from {dcm_dir} to NIFTI format...")

    # Get list of all DICOM files
    dcm_files = []
    for root, dirs, files in os.walk(dcm_dir):
        for file in files:
            if file.endswith('.dcm'):
                dcm_files.append(os.path.join(root, file))

    total_batches = (len(dcm_files) + batch_size - 1) // batch_size
    batch_tracker = [False] * total_batches

    # Load already completed batches from the processed log
    for root, dirs, files in os.walk(dcm_dir):
        for file in files:
            if file.endswith('.dcm'):
                dcm_file_path = os.path.join(root, file)
                if dcm_file_path in processed_files:
                    batch_index = dcm_files.index(dcm_file_path) // batch_size
                    batch_tracker[batch_index] = True

    # Process in batches
    for i in range(0, len(dcm_files), batch_size):
        batch_index = i // batch_size
        if batch_tracker[batch_index]:
            logging.info(f"Skipping batch {batch_index + 1} (already processed)")
            continue

        logging.info(f"Processing batch {batch_index + 1} of {total_batches}...")
        batch = dcm_files[i:i + batch_size]
        convert_batch(batch, nifti_dir)
        batch_tracker[batch_index] = True
        logging.info(f"Batch {batch_index + 1} of {total_batches} completed.")

    logging.info(f"All batches completed. Conversion completed. NIFTI files saved to {nifti_dir}")

# Run the conversion
convert_dicom_to_nifti(dcm_path, nifti_path, batch_size=100)
