# DEPENDENCIES

import os
import logging
from pathlib import Path

logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')

list_of_paths = [
    ".docker_ignore",
    ".env",
    ".gitignore",
    "Dockerfile",
    "env_setup.sh",
    "folder_structure.py",
    "LICENCE",
    "main.py",
    "README.md",
    "requirements.txt",
    "setup.py",
    "config/__init__.py",
    "config/config.py",
    "data/Medical_Book.pdf",
    "notebooks/Medical_Chatbot.ipynb",
    "src/llm/__init__.py",
    "src/llm/llm_builder.py",
    "src/prompts/__init__.py",
    "src/prompts/prompt_builder.py",
    "src/text_splitting/__init__.py",
    "src/text_splitting/split_text.py",
    "src/vector_index/__init__.py",
    "src/vector_index/index_manager.py",
    "src/utils/__init__.py",
    "src/utils/download_embeddings.py",
    "src/utils/load_pdf.py",
    "src/utils/logger.py",
    "web/__init__.py",
    "web/animations/chatbot.json",
    "web/animations/doctor.json",
    "web/static/style.css",
    "web/templates/chat.html",
    "web/app.py"
]


for path_str in list_of_paths:
    path = Path(path_str)

    if path_str.endswith("/"):  # Directory
        
        if not path.exists():
            os.makedirs(path, exist_ok=True)
            logging.info(f"Created directory: {path}")
        
        else:
            logging.info(f"Directory already exists: {path}")
    
    else:  # File
    
        if not path.exists():
    
            if not path.parent.exists():
                os.makedirs(path.parent, exist_ok=True)
                logging.info(f"Created parent directory: {path.parent} for the file: {path.name}")
    
            with open(path, "w") as f:
                pass
            logging.info(f"Created empty file: {path}")
    
        else:
            logging.info(f"File already exists: {path}")
