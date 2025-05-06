import os
from pathlib import Path

class Config:
    
    """
    Configuration class for storing credentials, file paths, and URLs.
    It also provides a method to ensure required directories exist.
    """
    EMBEDDING_MODEL_ID    = "sentence-transformers/all-MiniLM-L6-v2"
    MEDICAL_BOOK_DATA_DIR = "data/"

    INDEX_NAME            = "medical-chatbot"
    DIMENSION             = 384
    METRIC                = "cosine"
    CLOUD                 = "aws"
    REGION                = "us-east-1"

    LARGE_LANGUAGE_MODEL_ID = "llama3-8b-8192"

    @staticmethod
    def setup_directories():
        """
        Ensures that all required directories exist.
        If a directory does not exist, it creates it.
        """
        
        directories = []
        
        for directory in directories:
            
            if not os.path.exists(directory):
            
                os.makedirs(directory)
                print(f"Created directory: {directory}")
            
            else:
                print(f"Directory already exists: {directory}")