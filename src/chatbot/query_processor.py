from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
import logging
from src.utils.logger import setup_logger
from src.chatbot.llm_integration import process_query

logger = setup_logger()
MAX_CONTEXT_BYTES = 36000  # API byte limit buffer

def get_query_prompt():
    """
    Load query prompt template.
    
    Returns:
        PromptTemplate: Formatted prompt template.
    """
    try:
        template = """
        You are an assistant for querying a teacher registry dataset. The data contains:
        - School_Code: Unique school identifier
        - School_Name: Name of the school
        - Employee_Name: Name of the teacher
        - teacher_Code: Unique teacher identifier
        - Designation: Teacher's role (e.g., Lecturer, TGT)
        - Employee_Type: Employment type (e.g., Regular, Contract)
        - Is_Active?: Whether the teacher is active (Yes/No)

        Context: {context}

        User Query: {question}

        Provide a concise, accurate answer based on the data. If the query is unclear or data is insufficient, say so politely.
        """
        return PromptTemplate(
            input_variables=["context", "question"],
            template=template
        )
    except Exception as e:
        logger.error(f"Failed to load query prompt: {str(e)}")
        raise Exception(f"Failed to load query prompt: {str(e)}")

def truncate_context_bytes(text, max_bytes=MAX_CONTEXT_BYTES):
    """
    Truncate UTF-8 text to a safe byte limit.
    """
    if len(text.encode("utf-8")) <= max_bytes:
        return text
    return text.encode("utf-8")[:max_bytes].decode("utf-8", errors="ignore")

def process_query_with_prompt(chain, query, context=""):
    """
    Process query with prompt template, safely handling context size.
    
    Args:
        chain: ConversationalRetrievalChain instance.
        query (str): User query.
        context (str): Additional context from vector store.
    
    Returns:
        str: Formatted response.
    """
    try:
        if not query.strip():
            logger.warning("Empty query received")
            return "Please provide a valid query."

        # Safely truncate or split context if needed
        context = truncate_context_bytes(context, max_bytes=MAX_CONTEXT_BYTES - 5000)

        prompt = get_query_prompt()
        formatted_query = prompt.format(context=context, question=query)
        response = process_query(chain, formatted_query)
        return response

    except Exception as e:
        logger.error(f"Error processing query with prompt: {str(e)}")
        return f"Error processing query: {str(e)}"