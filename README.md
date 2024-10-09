# FTIR-Kramers-Kronig-Transformation
This Python project reads FTIR (Fourier-transform infrared spectroscopy) data, performs a **Kramers-Kronig transformation** on the reflectance data, and visualizes the resulting absorbance values. The transformation can help eliminate derivative peaks and highlight the true absorbance peaks in your spectra.
## Features
- Reads FTIR data from a tab-separated file with reflectance values.
- Performs a Kramers-Kronig transformation on the reflectance data to convert it into absorbance values.
- Uses **Hilbert transform** for calculating the imaginary part of the refractive index.
- Plots the absorbance spectrum against wavenumbers.
- Exports the transformed absorbance data as a CSV file.

## Getting Started

### Prerequisites

Make sure you have the following Python libraries installed:

- `numpy`
- `pandas`
- `matplotlib`
- `scipy`

You can install them using `pip`:

```bash
pip install numpy pandas matplotlib scipy
```
### Installation
1. Clone this repository to your local machine:
```bash
git clone https://github.com/kroumpas/FTIR-Kramers-Kronig-Transformation.git
```
2. Navigate to the project folder:
```bash
cd FTIR Kramers-Kronig Transformation
```
3. Place your FTIR.dat files in the same folder, or update the path in the script to point to the correct location.

### Usage
1. Modify the data loading part in the script to match your FTIR data format if necessary.
2. Run the Python script to perform the transformation.
```bash
python transform.py
```
3. After running the script, a plot of the absorbance vs wavenumbers will be displayed. The transformed data will be saved in a file name ftir_transformed.dat.

## Data Format
The script expects a tab-separated .dat file where:
- The first column is wavelength (unused in the script)
- The second column contains the wavenumbers (in units of 1/cm).
- The third column contains the reflectance values (decimal values are separated by commas).

### Customization
- You can change the input file by modifying this line in the script:
```bash
data = read_data('yourfile.dat')
```
- To save the plot as an image, you can add the following line after the plotting function:
```bash
plt.savefig('absorbance_plot.png')
```

### Citation

If you find this code useful in your research, please consider citing it as follows:
```bash
Konstantinos Roumpas. (2024). FTIR Kramers-Kronig Transformation [Computer Software]. GitHub. https://github.com/kroumpas/FTIR-Kramers-Kronig-Transformation ORCID: https://orcid.org/0009-0006-4187-438X
```
