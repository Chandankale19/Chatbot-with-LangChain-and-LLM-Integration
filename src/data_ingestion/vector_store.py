from langchain.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import logging
from src.utils.logger import setup_logger
from src.config import GOOGLE_API_KEY

logger = setup_logger()

def create_vector_store(df):
    """
    Create a Chroma vector store from DataFrame using Google Gemini embeddings,
    with safe chunking to avoid 400 errors for oversized payloads.

    Args:
        df (pd.DataFrame): Input DataFrame with teacher registry data.

    Returns:
        Chroma: Vector store instance.

    Raises:
        Exception: If vector store creation fails.
    """
    try:
        # Convert each row into a readable string
        texts = [str(row.to_dict()) for _, row in df.iterrows()]
        
        # Split texts safely using text splitter
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=3000,     # Stay well under 36000 bytes
            chunk_overlap=100
        )

        # Create LangChain Documents for better splitting
        docs = [Document(page_content=text) for text in texts]
        split_docs = splitter.split_documents(docs)

        logger.info(f"Total original rows: {len(texts)}, total chunks after split: {len(split_docs)}")

        # Initialize embeddings
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001",
            google_api_key=""
        )

        # Create vector store
        vector_store = Chroma.from_documents(
            documents=split_docs,
            embedding=embeddings,
            collection_name="teacher_registry"
        )

        logger.info(f"Created vector store with {len(split_docs)} documents")
        return vector_store

    except Exception as e:
        logger.error(f"Failed to create vector store: {str(e)}")
        raise Exception(f"Failed to create vector store: {str(e)}")
