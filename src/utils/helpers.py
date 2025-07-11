from tenacity import retry, stop_after_attempt, wait_exponential
import logging
from src.utils.logger import setup_logger

logger = setup_logger()

@retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=10))
def call_llm(llm, query):
    """
    Call LLM with retry logic.
    
    Args:
        llm: LLM instance.
        query (str): Query to process.
    
    Returns:
        Response from LLM.
    
    Raises:
        Exception: If all retries fail.
    """
    try:
        response = llm.invoke(query)
        logger.info(f"LLM call successful for query: {query[:50]}...")
        return response
    except Exception as e:
        logger.error(f"LLM call failed: {str(e)}")
        raise