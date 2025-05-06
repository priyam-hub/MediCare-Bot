# DEPENDENCIES

from ..utils.logger import LoggerSetup
from langchain_core.prompts import ChatPromptTemplate

#LOGGER SETUP
prompt_builder_logger = LoggerSetup(logger_name = "prompt_builder.py", log_filename_prefix = "prompt_builder").get_logger()

class PromptBuilder:
    """
    A class to build a structured chat prompt template for question-answering tasks.
    """

    def __init__(self) -> None:
        """
        Initializes the system prompt with guidance for the assistant.
        """

        try:
        
            self.system_prompt = (
                "You are an assistant for question-answering tasks. "
                "Use the following pieces of retrieved context to answer "
                "the question. If you don't know the answer, say that you "
                "don't know. Use three sentences maximum and keep the "
                "answer concise."
                "\n\n"
                "{context}"
            )

            prompt_builder_logger.info("PromptBuilder initialized successfully.")

        except Exception as e:
            prompt_builder_logger.error(f"Error initializing PromptBuilder: {repr(e)}")
            
            raise

    def build_prompt(self) -> ChatPromptTemplate:
        """
        Constructs the ChatPromptTemplate using the system and human message format.

        Returns:
        
            ChatPromptTemplate : A formatted prompt template for use in LLM chains.
        
        """
        try:
            
            prompt = ChatPromptTemplate.from_messages(
                [
                    ("system", self.system_prompt),
                    ("human", "{input}"),
                ]
            )

            prompt_builder_logger.info("Prompt built successfully.")
            
            return prompt
        
        except Exception as e:
            prompt_builder_logger.error(f"Error building prompt: {repr(e)}")
            
            raise
