<div align="center">

# 🤖 MediCare-Bot — Your trusted health companion.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-orange.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![LLaMA 3](https://img.shields.io/badge/LLaMA-3%208B-purple.svg)](https://ai.meta.com/llama/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue)](https://www.docker.com/)

*Supporting patients with trusted answers, one conversation at a time.*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Tech Stack](#-tech-stack) • [License](#-license) • [Contact](#-contact)

</div>

---

## 🌟 Overview

**MediCare-Bot** is designed to assist users with reliable and easy-to-understand health information. It learns from trusted medical books and uses intelligent search techniques to find the most relevant content. By combining smart retrieval with a powerful language model, the chatbot offers clear and accurate responses to medical queries, making healthcare information more accessible and conversational for everyone.

---

## 📚 Dataset

**Source:** [Medical Book Dataset – Kaggle](https://www.kaggle.com/datasets/abhirajmandal/medical-book)

#### 🔍 Description

This dataset contains textual content extracted from medical books, designed to provide structured and informative knowledge on a wide range of medical topics. It includes concise explanations, definitions, symptoms, causes, and treatments for various diseases and conditions. The dataset is ideal for building knowledge-driven applications like medical chatbots, as it captures essential clinical and healthcare-related information in a digestible format.

**Use Case:**
The dataset serves as the foundational knowledge base for the chatbot, allowing it to generate helpful and accurate responses to user queries by referencing real medical literature.

---

## 📌 Features

* **Patient-Centric Design**
  - Focused on delivering helpful and compassionate responses tailored to user needs.

* **Trusted Medical Knowledge**
  - Built using information from reliable medical books to ensure accuracy.

* **Natural Conversations**
  - Understands and responds in a human-like, conversational tone.

* **Instant Answers**
  - Provides quick and relevant responses to a wide range of medical questions.

* **Context-Aware**
  - Remembers and considers the context of your query for better responses.

* **User-Friendly Interface**
  - Simple and clean chat interface that's easy to use for everyone.

* **Secure and Private**
  - No personal data is stored or shared—ensuring privacy and confidentiality.

---

## 🛠️ Installation

### Step - 1: Repository Cloning

```bash
# Clone the repository
git clone https://github.com/priyam-hub/MediCare-Bot.git

# Navigate into the directory
cd MediCare-Bot
```

### Step - 2: Enviornmental Setup and Dependency Installation

```bash
# Run env_setup.sh
bash env_setup.sh

# Select 1 to create Python Environment
# Select 2 to create Conda Environment

# Python Version - 3.10
```

### Step - 3: Create a .env file in the root directory to add Credentials

```bash
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
GROQ_API_KEY  = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### Step - 4: Store the Vector Embeddings & Initialize RAG

```bash

# Run the Main Python Script
python main.py
```

### Step - 5: Run the Flask Server

```bash

# Run the Web App using Flask Server
python web/app.py
```

Upon running, navigate to the provided local URL in your browser to interact with the MediCare-Bot

---

## ⚙️ Technology Stack


* **Python** – Core programming language used for building the backend.
  🔗 [Install Python](https://www.python.org/downloads/)

* **PyTorch** – Deep learning framework used under the hood for embedding models and LLMs.
  🔗 [Install PyTorch](https://pytorch.org/get-started/locally/)

* **Transformers (Hugging Face)** – Used to load and manage pre-trained embedding models.
  🔗 [Transformers Documentation](https://huggingface.co/docs/transformers/index)

* **LangChain** – Framework for building applications with LLMs, supporting RAG and vector search.
  🔗 [LangChain Installation Guide](https://docs.langchain.com/docs/get_started/installation)

* **Flask** – Lightweight web framework to deploy the chatbot as a web API.
  🔗 [Flask Installation](https://flask.palletsprojects.com/en/latest/installation/)

---

### 🧠 Artificial Intelligence Models Stack

* **Vector Embedding – `sentence-transformers/all-MiniLM-L6-v2`**
  Lightweight and efficient embedding model for generating semantic vector representations of medical texts.
  🔗 [Model on Hugging Face](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)

* **Vector Database – Pinecone**
  High-performance vector store to manage and search large-scale embedding data.
  🔗 [Pinecone Documentation](https://docs.pinecone.io/docs/overview)

* **Information Retrieval – RAG (Retrieval-Augmented Generation)**
  Augments LLM responses by retrieving relevant content from medical embeddings.
  🔗 [RAG on LangChain](https://docs.langchain.com/docs/components/retrievers/)

* **Inference Engine – Groq**
  Ultra-fast inference platform to run LLaMa-3 and generate real-time answers.
  🔗 [Groq API](https://groq.com/)

* **Large Language Model – LLaMa-3 8B**
  Advanced open-source language model from Meta used for understanding medical context and generating responses.
  🔗 [LLaMa 3 (Meta)](https://ai.meta.com/llama/)

* **API Integration – Flask**
  Handles user requests and chatbot interactions through a simple web API.
  🔗 [Flask Official Docs](https://flask.palletsprojects.com/en/latest/)

* **Environmental Image – Docker**
  Ensures consistent, portable, and isolated runtime environment for the chatbot application.
  🔗 [Docker Installation](https://docs.docker.com/get-docker/)

* **Deployment – EC2 Instance**
  Scalable cloud server to host and serve the medical chatbot application.
  🔗 [Amazon EC2](https://aws.amazon.com/ec2/)

---

## 📁 Project Structure

```plaintext
MediCare-Bot/
├── .docker_ignore                            # Ignoring Files in Docker
├── .env                                      # Store the Pinecone and Groq Credentials
├── .gitignore                                # Ignoring files for Git
├── Dockerfile                                # Stored the Docker Setup
├── env_setup.sh                              # Package installation configuration
├── folder_structure.py                       # Contains the Project Folder Structure
├── LICENCE                                   # MIT License
├── main.py                                   # Store Vector Embeddings and Initialize the RAG
├── README.md                                 # Project documentation
├── requirements.txt                          # Python dependencies
├── setup.py                                  # Create the Project as Python Package
├── config/                                   # Configuration files
│   ├── __init__.py                           
│   └── config.py/                            # All Configuration Variables of Pipeline
├── data/                                     # Data directory
│   └── Medical_Book.pdf                      # Medical Book Dataset used for Vector Embedding
├── notebooks/                                # Jupyter notebooks for experimentation
│   └── Medical_Chatbot.ipynb                 # Experimented Chatbot in Jupyter Notebook
├── src/                                      # Source code
│   ├── llm/                                  # Large Language Model Directory
│   │   ├── __init__.py  
│   │   └── llm_builder.py                    # Python file to Build the LLM using ChatGroq                                       
│   ├── prompts/                              # System Prompt Directory
│   │   ├── __init__.py   
│   │   └── prompt_builder.py                 # Python file Build the Prompt for LLM Inference                                   
│   ├── text_splitting/                       # Text Splitting Directory
│   │   ├── __init__.py                           
│   │   └── split_text.py                     # Python File to Split the Text                                    
│   ├── vector_index/                         # Vector Index Directory
│   │   ├── __init__.py   
│   │   └── index_manager.py                  # Python file to create index in Vector DB                                            
│   └── utils/                                # Utility Functions Directory
│       ├── __init__.py                     
│       ├── download_embeddings.py            # Download the Embedding Model
│       ├── load_pdf.py                       # Load the PDF for Embedding
│       └── logger.py                         # Logger Setup
└── web/
    ├── __init__.py  
    ├── animations/                           
    │   ├── chatbot.json                      # Chatbot Animations
    │   └── doctor.json                       # Doctor Animations
    ├── static/                                
    │   ├── style.css                         # Styling of the Web Page
    ├── templates/                                
    │   ├── chat.html                         # Default Web Page
    └── app.py/                               # To run the flask server
        
```









