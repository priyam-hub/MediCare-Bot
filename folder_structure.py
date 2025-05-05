# DEPENDENCIES

import os
import logging
from pathlib import Path

logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')

list_of_paths    = ["config/__init__.py",
                    "config/config.py", 
                    "data", 
                    "database",
                    ]


for path in list_of_paths:
    path         = Path(path)

    if path.suffix: 
        
        if not path.parent.exists():
            os.makedirs(path.parent, exist_ok = True)
            
            logging.info(f"Creating directory: {path.parent} for the file: {path.name}")

        if not path.exists() or path.stat().st_size == 0:
           
            with open(path, "w") as f:
                pass
            
            logging.info(f"Creating empty file: {path}")
        
        else:
            logging.info(f"{path.name} already exists")
    
    else:
        os.makedirs(path, exist_ok = True)
        logging.info(f"Creating directory: {path}")
