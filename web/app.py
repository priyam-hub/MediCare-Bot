# DEPENDENCIES

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from json import load
from flask import Flask
from pathlib import Path
from flask import jsonify
from flask import request
from dotenv import load_dotenv
from config.config import Config
from flask import render_template
from src.utils.logger import LoggerSetup
from src.llm.llm_builder import LLMBuilder
from langchain_pinecone import PineconeVectorStore
from langchain.chains import create_retrieval_chain
from src.prompts.prompt_builder import PromptBuilder
from src.utils.download_embeddings import EmbeddingDownloader
from langchain.chains.combine_documents import create_stuff_documents_chain

import warnings
warnings.filterwarnings(action = "ignore")

# LOADING ENVIRONMENT VARIABLES
dotenv_path                     = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path = dotenv_path)

PINECONE_API_KEY                = os.environ.get('PINECONE_API_KEY')
GROQ_API_KEY                    = os.environ.get('GROQ_API_KEY')

print(f"Pinecone API Key: {PINECONE_API_KEY}")
print(f"GROQ API Key: {GROQ_API_KEY}")

app                             = Flask(__name__)

# LOGGER SETUP
app_logger                      = LoggerSetup(logger_name = "app.py", log_filename_prefix = "app").get_logger()

embedder                        = EmbeddingDownloader(model_name = Config.EMBEDDING_MODEL_ID)
embeddings                      = embedder.load_embeddings()

docsearch                       = PineconeVectorStore.from_existing_index(index_name  = Config.INDEX_NAME,
                                                                          embedding   = embeddings
                                                                          )
        
retriever                       = docsearch.as_retriever(search_type    = "similarity",
                                                         search_kwargs  = {"k":5})

app_logger.info(f"Retireval Augmented Generation (RAG) Chain Initialized Successfully")

prompt_builder                  = PromptBuilder()
prompt                          = prompt_builder.build_prompt()

llm_builder                     = LLMBuilder(api_key      = GROQ_API_KEY, 
                                             temperature  = 0.4, 
                                             model_name   = Config.LARGE_LANGUAGE_MODEL_ID
                                             )

llm                             = llm_builder.build_llm()

app_logger.info("Prompt and Large Language Model Initialized Successfully")

question_answer_chain           = create_stuff_documents_chain(llm, prompt)
rag_chain                       = create_retrieval_chain(retriever, question_answer_chain)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/medical_chat", methods = ["GET", "POST"])
def chat():
    try:
        app_logger.info("Chatbot is running")
        msg       = request.form["msg"]
        input     = msg
        app_logger.info(input)
        
        response  = rag_chain.invoke({"input": msg})
        app_logger.info(f"Response: {response['answer']}")
        
        return str(response["answer"])
    
    except Exception as e:
        app_logger.error(f"Error Occurred in Chat API: {repr(e)}")
        
        return str(e)


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 8080, debug = True, use_reloader = False)