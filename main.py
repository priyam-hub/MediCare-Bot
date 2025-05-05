from config.config import Config
from src.utils.logger import LoggerSetup
from src.utils.load_pdf import PDF_Loader
from src.text_splitting.split_text import TextSplitter

# LOGGER SETUP
main_logger = LoggerSetup(logger_name = "main.py", log_filename_prefix = "main").get_logger()

def main():

    try:

        pdf_loader = PDF_Loader(directory_path = Config.MEDICAL_BOOK_DATA_DIR)

        documents  = pdf_loader.load_pdfs() 
        main_logger.info(f"Loaded {len(documents)} documents from {Config.MEDICAL_BOOK_DATA_DIR}")

        splitter   = TextSplitter(chunk_size = 500, chunk_overlap = 20)
        chunks     = splitter.split_text(documents)
        main_logger.info(f"Split documents into {len(chunks)} chunks.")

    except Exception as e:
        main_logger.error(f"Error Occurred in Main Function: {repr(e)}")

        raise e
    
if __name__ == "__main__":
    main()

