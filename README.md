# Access UK Radar observations

<img width="309" height="57" alt="UKCEH and FDRI logos" src="https://github.com/user-attachments/assets/04afdc63-663f-41e4-b29d-9419f78d76c3" />
</br>

**Author:** [Tom Keel](https://github.com/Thomasjkeel).


## Description
This repo goes through how to load in and subset radar data from the following three sources:
1. Met Office Rain Radar Data from the NIMROD System from the CEDA Archive [link](https://catalogue.ceda.ac.uk/uuid/82adec1f896af6169112d09cc1174499/?q=&results_per_page=20&sort_by=title_desc&objects_related_to_uuid=82adec1f896af6169112d09cc1174499&page=3)   
2. Met Office UK Radar Observations on a 2-year rolling archive from the Registry of Open Data on AWS [link](https://registry.opendata.aws/met-office-uk-radar-observations/)
3. How to read NIMROD data from JASMIN


| Dataset | Location | Python Notebook |
| ------- | -------- | --------------- |
| Met Office UK Radar Observations  | [Registry of Open Data on AWS](https://registry.opendata.aws/met-office-uk-radar-observations/) | [aws_radar_subset_workflow.ipynb](https://github.com/Thomasjkeel/access-UK-radar-data/blob/main/MORadarObs-OpenDataRegistry/aws_radar_subset_workflow.ipynb) |
| Met Office Rain Radar Data from the NIMROD System | [CEDA Archive](https://catalogue.ceda.ac.uk/uuid/82adec1f896af6169112d09cc1174499/) | [read_in_NIMROD_radar_data.ipynb](https://github.com/Thomasjkeel/access-UK-radar-data/blob/main/NIMROD-CEDAArchive/read_in_NIMROD_radar_data.ipynb) |
| Met Office Rain Radar Data from the NIMROD System | [JASMIN](https://www.jasmin.ac.uk/about/) | [read_in_NIMROD_radar_data.ipynb](https://github.com/Thomasjkeel/access-UK-radar-data/blob/main/NIMROD-CEDAArchive/read_in_NIMROD_radar_data.ipynb) |


## About this work
This work was carried as part of the UK Government funded [Floods and Droughts Research Infrastructure (FDRI)](https://fdri.org.uk/) project. In this project we are improving access to radar datasets.


## How to run these notebooks

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

- You will need to [apply for access to the FDRI Group Workspace](https://accounts.jasmin.ac.uk/services/group_workspaces/fdri/) to be able to use the pre-installed environment for running the notebooks
- Once access has been granted, open up the [JASMIN Notebook Service](https://notebooks.jasmin.ac.uk/)
- Obtain a copy of the notebooks by clicking the 'Git' in the menu bar at the top of the webpage, then 'Clone a Repository'. Tick the 'Download the repository' button, and paste in the link to the repository: https://github.com/NERC-CEH/fdri-gridded-notebooks.git (this can also be obtained by clicking the big green '<> Code' button on the repository main page, clicking 'HTTPS' and copying the link shown).
- The environment for running the notebooks is pre-installed but a couple of steps are required to enable it for running notebooks the first time you use the Notebook Service:
- Open up a terminal and run ```conda activate /gws/ssde/j25b/fdri/envs/fdricombo``` to activate the environment, then
- ```python -m ipykernel install --user --name fdricombo``` to install the 'kernel' (the Python executable) to your local user area
- After, you can load the notebook you wish to run from the files panel on the left, selecting the just-installed kernel (called fdricombo) by clicking the text next to the small empty circle top right of the notebook, that says 'No Kernel' or 'Python' or similar, and selecting 'fdricombo' from the menu that appears. Note that it may take a few minutes to show up when first installing the kernel. 
- Next time you want to run the notebook (or any Python notebook), you can just revisit the JASMIN notebook service, load the notebook, and it should pick up the environment with all the installed packages in it automatically.
