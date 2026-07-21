# Access UK Radar observations

<img width="309" height="57" alt="UKCEH and FDRI logos" src="https://github.com/user-attachments/assets/04afdc63-663f-41e4-b29d-9419f78d76c3" />
</br>

**Author:** [Tom Keel](https://github.com/Thomasjkeel).

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Thomasjkeel/access-UK-radar-data/HEAD)

## Description
This repo goes through how to load in and subset radar data from the following two sources:

| Source | Dataset | Location | Python Notebook |
| ------ | ------- | -------- | --------------- |
| from file | Met Office Rain Radar Data from the NIMROD System (2002-present; 5 or 15 min resolution) | [CEDA Archive](https://catalogue.ceda.ac.uk/uuid/82adec1f896af6169112d09cc1174499/) | [read_radar_data_from_CEDA_Archive.ipynb](https://github.com/Thomasjkeel/access-UK-radar-data/blob/main/notebooks/from_file/read_radar_data_from_CEDA_Archive.ipynb) |
| from cloud | Met Office UK Radar Observations composites (2-year rolling; 15 min resolution)  | [Registry of Open Data on AWS](https://registry.opendata.aws/met-office-uk-radar-observations/) | [read_radar_data_from_open_data_registry.ipynb](https://github.com/Thomasjkeel/access-UK-radar-data/blob/main/notebooks/from_cloud/read_radar_data_from_open_data_registry.ipynb) |

## Gallery

<p float="left">
    <img src="https://raw.githubusercontent.com/Thomasjkeel/access-UK-radar-data/refs/heads/main/figures/UK_rain_from_radar_5min.png" alt="5min-mean" style="width:250px;"/>
    <img src="https://raw.githubusercontent.com/Thomasjkeel/access-UK-radar-data/refs/heads/main/figures/UK_rain_from_radar_1h_mean.png" alt="1h-mean" style="width:250px;" />
</p>

<img src="https://raw.githubusercontent.com/Thomasjkeel/access-UK-radar-data/refs/heads/main/figures/severn_catchment_subset_1h_mean.png" alt="catch-subset" style="width:500px;"/>
<img src="https://raw.githubusercontent.com/Thomasjkeel/access-UK-radar-data/refs/heads/main/figures/catchment_mean_rainfall.png" alt="catch-subset" style="width:500px;" />


## How to run these notebooks
### Requirements
| Package | version | Use |
| ------- | ------- | --- |
| numpy | | data |
| xarray[io] | | data |
| matplotlib | | plotting |
| rioxarray | | spatial |
| rasterio | | spatial |
| geopandas | | spatial |
| cartopy | | spatial |
| pyproj | | spatial |
| boto3 | | cloud read |
| botocore | | cloud read |
| s3fs | | cloud read |

<details>
    <summary><i><b>If you are not intending to run these notebooks locally, please click here for running options.</i></b></b></summary>

### Google Colab
**Google Account required**
- Click the "Launch in Colab" button at the top of the notebook.
- Sign in to your google account if needed (blue "Sign in" button in the top right)
- Each notebook includes a cell near the top for installing extra packages not available in the default Colab environment. Run it to install these.

**Note:** Changes you make to the notebook will not be saved by default. If you wish to save your changes, click the "Copy to Drive" text just below the menu bar at the top of the screen. This will create a separate copy of the notebook in your Google Drive and any edits you make will be saved to it.

### Binder
Click the "Launch Binder" button at the top of the notebook. Please note that it may take several minutes to load the environment. After the environment has loaded the notebook will appear and you will be able to run it. 

**Note:** Changes you make to the notebook will not be saved. There is no easy way to save edits you make when using the Binder service.

### JASMIN Notebook Service
[JASMIN](https://www.jasmin.ac.uk/about/) is a computing and data storage resource and environment for NERC researchers. If you have an account, you can make use of their own notebook service to run these notebooks. We are working on simplifying the setup, as it is a little more complicated than using Google Colab or Binder at present. For now, instructions are provided below and on the [JASMIN documentation website](https://help.jasmin.ac.uk/docs/interactive-computing/jasmin-notebooks-service/). As JASMIN is also where the datasets are stored, running notebooks from JASMIN has the advantage of faster data access times as where you are running the notebooks is physically closer to where the data is stored. 

- Once access has been granted, open up the [JASMIN Notebook Service](https://notebooks.jasmin.ac.uk/)
- Obtain a copy of the notebooks by clicking the 'Git' in the menu bar at the top of the webpage, then 'Clone a Repository'. Tick the 'Download the repository' button, and paste in the link to the repository: https://github.com/NERC-CEH/fdri-gridded-notebooks.git (this can also be obtained by clicking the big green '<> Code' button on the repository main page, clicking 'HTTPS' and copying the link shown).

</details>

## About this work
This work was carried as part of the UK Government funded [Floods and Droughts Research Infrastructure (FDRI)](https://fdri.org.uk/) project. In this project we are improving access to radar datasets.
