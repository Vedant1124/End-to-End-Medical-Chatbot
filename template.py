# Instead of executing all the files we will run this temmpelate.py to execute our whole project it will create all the necessary files required
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    "src\__init__.py",
    "src\helper.py",
    "src\prompt.py",
    ".env",
    "setup.py",
    "research/trials.ipynb",
    "app.py",
    "store_index.py",
    "static\.gitkeep",
    "templates\chat.html"
]

for filepath in list_of_files:
    filepath=Path(filepath) # With the help of This Path Class it will convert the filepath according to the operating system like windows , mac or linux

    # Now we have to separate the folders and files using os.path.split function it will separate (for ex) the "src" folder and the "__init__.py" file present in the folder
    filedir , filename = os.path.split(filepath)
    
    # If filedir exist create a directory of filedir and logging the changes
    if filedir !="":
        os.makedirs(filedir , exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    # if filepath does not exist in the directory
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file:{filepath}")

    else:
        logging.info(f"{filename} is already created")
