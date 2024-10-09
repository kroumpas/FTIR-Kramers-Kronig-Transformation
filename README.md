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
