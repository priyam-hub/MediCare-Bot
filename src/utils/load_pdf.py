# DEPENDENCIES

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import DirectoryLoader

from .logger import LoggerSetup

# LOGGER SETUP
pdf_logger = LoggerSetup(logger_name = "load_pdf.py", log_filename_prefix = "load_pdf").get_logger()

class PDF_Loader:
    """
    A class to load all PDF files from a specified directory using PyPDFLoader.
    """

    def __init__(self, directory_path : str) -> None:
        """
        Initialize with the path to the directory containing PDF files.

        Arguments:
        
            `directory_path`        {str}      : Path to the PDF directory.
        
        """
        try:

            self.directory_path = directory_path
            pdf_logger.info(f"PDF_Loader Class Initialized Successfully")

        except Exception as e:
            pdf_logger.error(f"Error initializing PDF_Loader: {repr(e)}")
            
            raise e

    def load_pdfs(self) -> list:
        """
        Loads all PDF files from the initialized directory.

        Returns:
            
            `documents`        {list}        : A list of LangChain Document objects loaded from the PDF files.
        
        """
        try:

            loader    = DirectoryLoader(self.directory_path,
                                        glob        = "*.pdf",
                                        loader_cls  = PyPDFLoader
                                        )
            
            documents = loader.load()
            pdf_logger.info(f"Loaded {len(documents)} PDF files from {self.directory_path}")
            
            return documents
        
        except Exception as e:
            pdf_logger.error(f"Error loading PDFs: {repr(e)}")
            
            raise e
