# DEPENDENCIES

from langchain_groq import ChatGroq
from ..utils.logger import LoggerSetup

#LOGGER SETUP
llm_builder_logger = LoggerSetup(logger_name = "llm_builder.py", log_filename_prefix = "llm_builder").get_logger()

class LLMBuilder:
    """
    A class to build and configure a ChatGroq language model for text generation.
    """

    def __init__(self, api_key : str, temperature : float = 0.4, model_name : str = "llama3-8b-8192"):
        """
        Initializes the LLMBuilder with specified parameters.

        Arguments:

            api_key            {str}        : The API key for authenticating with Groq.
        
            temperature       {float}       : Sampling temperature to control randomness in output.
            
            model_name         {str}        : The name of the Groq model to use.
        """
        try:
            self.api_key      = api_key
            self.temperature  = temperature
            self.model_name   = model_name

            llm_builder_logger.info("LLMBuilder initialized successfully.")

        except Exception as e:
            llm_builder_logger.error(f"Error initializing LLMBuilder: {repr(e)}")
            
            raise

    def build_llm(self) -> ChatGroq:
        """
        Creates and returns an instance of ChatGroq with the specified settings.

        Returns:
        
            ChatGroq : Configured language model instance for inference.
        
        """
        try:

            llm = ChatGroq(temperature   = self.temperature,
                           groq_api_key  = self.api_key,
                           model_name    = self.model_name
                           )
            
            llm_builder_logger.info("LLM built successfully.")
            
            return llm
        
        except Exception as e:
            llm_builder_logger.error(f"Error building LLM: {repr(e)}")
            
            raise
