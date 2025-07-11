from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import logging
from src.utils.logger import setup_logger
from src.chatbot.llm_integration import initialize_llm

logger = setup_logger()

def initialize_chain(vector_store):
    """
    Initialize LangChain ConversationalRetrievalChain with memory.
    
    Args:
        vector_store: Chroma vector store instance.
    
    Returns:
        ConversationalRetrievalChain: Initialized chain.
    
    Raises:
        Exception: If chain initialization fails.
    """
    try:
        llm = initialize_llm()
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            max_token_limit=1000
        )
        chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vector_store.as_retriever(search_kwargs={"k": 5}),
            memory=memory,
            return_source_documents=True
        )
        logger.info("Initialized ConversationalRetrievalChain")
        return chain
    except Exception as e:
        logger.error(f"Failed to initialize chain: {str(e)}")
        raise Exception(f"Failed to initialize chain: {str(e)}")