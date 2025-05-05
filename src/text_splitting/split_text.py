# DEPENDENCIES

from langchain.text_splitter import RecursiveCharacterTextSplitter

from ..utils.logger import LoggerSetup

# LOGGER SETUP
split_text_logger = LoggerSetup(logger_name = "split_text.py", log_filename_prefix = "split_text").get_logger()

class TextSplitter:
    """
    A class to split extracted documents into smaller text chunks using RecursiveCharacterTextSplitter.
    
    """

    def __init__(self, chunk_size : int = 500, chunk_overlap : int = 20) -> None:
        """
        Initialize the text splitter with specified chunk size and overlap.

        Arguments:
        
            `chunk_size`               {int}          : Maximum size of each text chunk.
            
            `chunk_overlap`            {int}          : Number of overlapping characters between chunks.
        
        """
        try:
            if chunk_size <= 0:
                split_text_logger.error("Chunk size must be a positive integer.")
                raise ValueError("Chunk size must be a positive integer.")
            
            if chunk_overlap < 0:
                split_text_logger.error("Chunk overlap must be a non-negative integer.")
                raise ValueError("Chunk overlap must be a non-negative integer.")
            
            self.chunk_size     = chunk_size
            self.chunk_overlap  = chunk_overlap
            self.text_splitter  = RecursiveCharacterTextSplitter(chunk_size      = self.chunk_size,
                                                                chunk_overlap   = self.chunk_overlap
                                                                )
            split_text_logger.info(f"TextSplitter initialized with chunk size: {self.chunk_size} and chunk overlap: {self.chunk_overlap}.")

        except Exception as e:
            split_text_logger.error(f"Error initializing TextSplitter: {repr(e)}")
            
            raise e

    def split_text(self, extracted_data : list) -> list:
        """
        Splits the input documents into smaller text chunks.

        Arguments:
        
            `extracted_data`      {list}        : A list of documents (typically from PDF loaders).

        
        Returns:
        
            `text_chunks`         {list}        : A list of smaller text chunks.
        
        """
        try:
            
            if not isinstance(extracted_data, list):
                split_text_logger.error("Input data must be a list of documents.")
            
                raise TypeError("Input data must be a list of documents.")
            
            if len(extracted_data) == 0:
                split_text_logger.error("Input data list is empty.")
            
                raise ValueError("Input data list is empty.")
            
            text_chunks = self.text_splitter.split_documents(extracted_data)
            split_text_logger.info(f"Split {len(extracted_data)} documents into {len(text_chunks)} text chunks.")
            
            return text_chunks
        
        except Exception as e:
            split_text_logger.error(f"Error splitting text: {repr(e)}")
            
            raise e
