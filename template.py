import os
from pathlib import Path
import logging

#logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project_name = "KidneyDiseaseClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test/test.py"]

for file in list_of_files:
    filevar = Path(file)
    filedir,filename = os.path.split(filevar)

    if(filedir != ""):
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Creating Directory; {filedir} for the file : {filename}")

    if(not os.path.exists(filevar)) or (os.path.getsize(filevar) == 0):
        with open (filevar,"w") as f:
            pass
            logging.info(f"Creating empty file : {filevar}")
        
    else:
        logging.info(f"{filename} already exists")

