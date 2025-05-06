# DEPENDENCIES

import os
import sys
from json import load
from dotenv import load_dotenv
from config.config import Config
from src.utils.logger import LoggerSetup
from src.utils.load_pdf import PDF_Loader
from langchain_pinecone import PineconeVectorStore
from src.text_splitting.split_text import TextSplitter
from src.utils.download_embeddings import EmbeddingDownloader
from src.vector_index.index_manager import PineconeIndexManager

import warnings
warnings.filterwarnings(action = "ignore")

# LOADING ENVIRONMENT VARIABLES
load_dotenv()
PINECONE_API_KEY                = os.environ.get('PINECONE_API_KEY')
os.environ["PINECONE_API_KEY"]  = PINECONE_API_KEY

# LOGGER SETUP
main_logger                     = LoggerSetup(logger_name = "main.py", log_filename_prefix = "main").get_logger()

def main():

    try:

        pdf_loader              = PDF_Loader(directory_path = Config.MEDICAL_BOOK_DATA_DIR)

        documents               = pdf_loader.load_pdfs() 
        main_logger.info(f"Loaded {len(documents)} documents from {Config.MEDICAL_BOOK_DATA_DIR}")

        splitter                = TextSplitter(chunk_size = 500, chunk_overlap = 20)
        chunks                  = splitter.split_text(documents)
        main_logger.info(f"Split documents into {len(chunks)} chunks.")

        embedder                = EmbeddingDownloader(model_name = Config.EMBEDDING_MODEL_ID)
        embeddings              = embedder.load_embeddings()

        # query_result            = embeddings.embed_query("Hello world")
        # print("Length", len(query_result))

        # index_manager           = PineconeIndexManager(api_key     = PINECONE_API_KEY, 
        #                                                index_name  = Config.INDEX_NAME, 
        #                                                dimension   = Config.DIMENSION, 
        #                                                metric      = Config.METRIC, 
        #                                                cloud       = Config.CLOUD, 
        #                                                region      = Config.REGION
        #                                                )
        # index_manager.create_index()

        # main_logger.info(f"Created index {Config.INDEX_NAME} with dimension {Config.DIMENSION} and metric {Config.METRIC}.")

        # docsearch               = PineconeVectorStore.from_documents(documents   = chunks,
        #                                                              index_name  = Config.INDEX_NAME,
        #                                                              embedding   = embeddings,
        #                                                              )
        
        docsearch               = PineconeVectorStore.from_existing_index(index_name  = Config.INDEX_NAME,
                                                                          embedding   = embeddings
                                                                          )
        
        retriever               = docsearch.as_retriever(search_type    = "similarity",
                                                         search_kwargs  = {"k":5})
        
        main_logger.info(f"Created retriever with {len(docsearch)} documents.")
        
    except Exception as e:
        main_logger.error(f"Error Occurred in Main Function: {repr(e)}")

        raise e
    
if __name__ == "__main__":
    main()

