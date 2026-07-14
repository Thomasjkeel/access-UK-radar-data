import gzip
import os
import nimrod
import xarray as xr


PATH_TO_NIMROD_FOLDER = "path/to/data/"
GZIP_DATA_NAME = "metoffice-c-band-rain-radar_uk_????_1km-composite.dat.gz"
OUTPUT_FOLDER = "path/to/output/"

with gzip.open(os.path.join(PATH_TO_NIMROD_FOLDER, GZIP_DATA_NAME), "rb") as f:
    with open(os.path.join(PATH_TO_NIMROD_FOLDER, "decompressed.dat"), "wb") as f_out:
        f_out.write(f.read())

# Extrac
nimrod_data = nimrod.Nimrod(open(os.path.join(OUTPUT_FOLDER, "decompressed.dat"), "rb"))
nimrod_data.extract_asc(
    open(os.path.join(OUTPUT_FOLDER, "datetime_nimrod_raster.dat"), "w")
)

# Load the full raster with xarray:
example_nimrod_raster = xr.open_dataarray(
    os.path.join(OUTPUT_FOLDER, "datetime_nimrod_raster.dat")
)
