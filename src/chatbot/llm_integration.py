from langchain_google_genai import ChatGoogleGenerativeAI
from tenacity import retry, stop_after_attempt, wait_exponential
import logging
from src.utils.logger import setup_logger
from src.config import GOOGLE_API_KEY

logger = setup_logger()

@retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=10))
def initialize_llm():
    """
    Initialize Google Gemini LLM with retry logic.
    
    Returns:
        ChatGoogleGenerativeAI: Initialized LLM instance.
    
    Raises:
        Exception: If LLM initialization fails after retries.
    """
    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",
            google_api_key="",
            temperature=0.7,
            max_output_tokens=2048
        )
        logger.info("Successfully initialized Gemini LLM")
        return llm
    except Exception as e:
        logger.error(f"Failed to initialize Gemini LLM: {str(e)}")
        raise Exception(f"Failed to initialize Gemini LLM: {str(e)}")

@retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=10))
def process_query(chain, query):
    """
    Process a user query using the LangChain chain.
    
    Args:
        chain: ConversationalRetrievalChain instance.
        query (str): User query.
    
    Returns:
        str: Response from the LLM.
    
    Raises:
        Exception: If query processing fails after retries.
    """
    try:
        response = chain.invoke({"question": query})
        answer = response.get("answer", "No answer provided")
        logger.info(f"Processed query: {query[:50]}... Response: {answer[:50]}...")
        return answer
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        raise Exception(f"Error processing query: {str(e)}")