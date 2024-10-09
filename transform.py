import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import hilbert

# Read the data (!) Configure this to match your data type - This version reads tab-separated values and considers ',' to be a decimal point.
def read_data(file_path):
    return pd.read_csv(file_path, delimiter='\t', decimal=',')

# Function to perform the Kramers-Kronig transformation
def kramers_kronig(reflectance, wavenumbers):
    # Convert reflectance to a complex refractive index using the K-K relation
    n = reflectance  # Real part approximation (reflectance is real)
    
    # Use Hilbert transform to calculate the imaginary part of the refractive index
    k = np.imag(hilbert(np.log(reflectance)))
    
    # Calculate absorbance using the relation A = 4 * pi * k / lambda
    absorbance = 4 * np.pi * k / wavenumbers
    
    return absorbance

# Read_data
data = read_data('your-data.dat')

# Extract the wavenumbers and reflectance columns
wavenumbers = data.iloc[:, 1].values  # Second column: Wavenumbers
reflectance = data.iloc[:, 2].values  # Third column: Reflectance

# Perform Kramers-Kronig transformation
absorbance = kramers_kronig(reflectance, wavenumbers)

# Plot the results
plt.figure(figsize=(10,6))
plt.plot(wavenumbers, absorbance)
plt.xlabel('Wavenumbers [1/cm]')
plt.ylabel('Absorbance')
plt.title('Kramers-Kronig Transformed FTIR Absorbance')
plt.legend()
plt.grid(True)
plt.show()

# Optionally save the transformed data to CSV
transformed_data = pd.DataFrame({
    'Wavenumbers [1/cm]': wavenumbers,
    'Absorbance': absorbance
})

transformed_data.to_csv('ftir_transformed.csv', index=False)
