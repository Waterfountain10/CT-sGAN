
# DeepFake Medical Imagery (CT-sGAN)

This project aims to generate fake oncology CT scans using GANs.

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Waterfountain10/CT-sGAN.git
   cd CT-sGAN
   ```

2. **Create a Virtual Environment and Install Dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Download Data:**
   Download the DICOM files from [TCIA](https://www.cancerimagingarchive.net/collection/prostate-mri-us-biopsy/) using the NBIA Data Retriever. The data will be in a nested directory structure.

4. **Convert DICOM to NIFTI:**
   ```bash
   python scripts/convert_dicom_to_nifti.py
   ```

## Directory Structure

```
CT_sGAN/
├── data/
│   ├── dcm/            # Raw DICOM files (downloaded data)
│   ├── nifti/          # Converted NIFTI files
├── notebooks/          # Jupyter notebooks for experiments
├── scripts/            # Python scripts for processing and training
│   ├── convert_dicom_to_nifti.py
│   ├── train_dcgan.py
│   ├── model.py
│   ├── utils.py
├── models/             # Saved GAN models
├── results/            # Generated images and evaluation results
├── .gitignore
├── README.md
└── requirements.txt
```

## Running the GAN Model

1. **Train the Model:**
   Add your training script here.

2. **Generate Images:**
   Add your image generation script here.

## License

This project is licensed under the MIT License.