# DEPENDENCIES

from torch import log_
from langchain_community.embeddings import HuggingFaceEmbeddings

from .logger import LoggerSetup

# LOGGER SETUP
embedding_logger = LoggerSetup(logger_name = "download_embeddings.py", log_filename_prefix = "download_embeddings").get_logger()

class EmbeddingDownloader:
    """
    A class to download and initialize Hugging Face embeddings using the specified transformer model.
    """

    def __init__(self, model_name : str = 'sentence-transformers/all-MiniLM-L6-v2') -> None:
        """
        Initializes the embedding model.

        Arguments:
            
            `model_name`                 {str}           : Name of the Hugging Face model to use for embeddings.
                                                           Defaults to 'sentence-transformers/all-MiniLM-L6-v2'.
        """
        try:
        
            self.model_name = model_name
            embedding_logger.info(f"Initializing Hugging Face Embeddings with model: {self.model_name}")

        except Exception as e:
            embedding_logger.error(f"Error Occurred in EmbeddingDownloader: {repr(e)}")
            
            raise e

    def load_embeddings(self) -> HuggingFaceEmbeddings:
        """
        Loads the Hugging Face embedding model.

        Returns:
        
            `embeddings`          {HuggingFaceEmbeddings}       : An instance of the HuggingFaceEmbeddings model.
        
        """
        try:
            embeddings = HuggingFaceEmbeddings(model_name = self.model_name)
            embedding_logger.info(f"Successfully loaded Hugging Face Embeddings with model: {self.model_name}")
            
            return embeddings
        
        except Exception as e:
            embedding_logger.error(f"Error Occurred in load_embeddings: {repr(e)}")
            
            raise e