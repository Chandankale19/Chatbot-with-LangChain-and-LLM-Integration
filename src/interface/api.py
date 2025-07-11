from fastapi import APIRouter, UploadFile, File, HTTPException, Form, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd
import logging
from src.utils.logger import setup_logger
from src.data_ingestion.excel_reader import read_excel
from src.data_ingestion.vector_store import create_vector_store
from src.chatbot.langchain_core import initialize_chain
from src.chatbot.query_processor import process_query_with_prompt
from pydantic import BaseModel
from typing import Optional
import gdown
from pandas import read_excel
from src.state import global_state  # or wherever you're storing state
import re
import numpy as np
import tempfile
import os

logger = setup_logger()

router = APIRouter()

# Mount templates and static files
templates = Jinja2Templates(directory="src/templates")
router.mount("/static", StaticFiles(directory="src/static"), name="static")

# Global state (in production, use a proper state management solution)
global_state = {
    "vector_store": None,
    "chain": None,
    "df": None
}

class QueryRequest(BaseModel):
    query: str

@router.get("/", response_class=HTMLResponse)
async def get_index():
    """
    Serve the main HTML page.
    """
    return templates.TemplateResponse("index.html", {"request": {}})

def extract_drive_file_id(url: str) -> str:
    """
    Extracts the Google Drive file ID from a shareable link or returns the raw ID if given.

    Args:
        url (str): Shareable Google Drive URL or file ID.

    Returns:
        str: Extracted file ID.

    Raises:
        ValueError: If file ID cannot be extracted.
    """
    patterns = [
        r"https?://drive\.google\.com/file/d/([a-zA-Z0-9_-]+)",
        r"https?://docs\.google\.com/spreadsheets/d/([a-zA-Z0-9_-]+)",
        r"https?://drive\.google\.com/open\?id=([a-zA-Z0-9_-]+)",
        r"id=([a-zA-Z0-9_-]+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    # If it's already an ID
    if re.fullmatch(r"[a-zA-Z0-9_-]{20,}", url):
        return url

    raise ValueError("Invalid Google Drive URL or File ID.")

@router.post("/fetch_from_drive")
async def fetch_from_drive(file_url: str = Query(..., description="Google Drive shareable link or file ID")):
    """
    Fetch an Excel file from Google Drive and process it.

    Args:
        file_url (str): Shareable Google Drive link or File ID.

    Returns:
        dict: Status and preview of the data.
    """
    try:
        file_id = extract_drive_file_id(file_url)
        download_url = f"https://drive.google.com/uc?id={file_id}"
        output_file = os.path.join(tempfile.gettempdir(), "teacher_registry.xlsx")

        gdown.download(download_url, output_file, quiet=False)

        df = read_excel(output_file)
        global_state["df"] = df

        global_state["vector_store"] = create_vector_store(df)
        global_state["chain"] = initialize_chain(global_state["vector_store"])

        # Replace NaN/inf for JSON serialization
        safe_df = df.head(5).replace([np.nan, np.inf, -np.inf], None)
        preview = safe_df.to_dict(orient="records")


        logger.info("Excel file fetched and processed successfully from Google Drive")
        return {
            "status": "success",
            "message": "File fetched and processed successfully",
            "preview": preview
        }

    except ValueError as ve:
        logger.error(f"ValueError during file fetch: {str(ve)}")
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        logger.error(f"Error fetching file from Google Drive: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error fetching file: {str(e)}")
    
@router.post("/query")
async def process_query(request: QueryRequest):
    """
    Process a user query.
    
    Args:
        request: QueryRequest with query string.
    
    Returns:
        dict: Query response.
    
    Raises:
        HTTPException: If query processing fails or no file is uploaded.
    """
    try:
        if not global_state["chain"] or not global_state["vector_store"]:
            logger.error("No file uploaded or processed")
            raise HTTPException(status_code=400, detail="No file uploaded. Please upload an Excel file first.")
        
        query = request.query
        response = process_query_with_prompt(
            global_state["chain"],
            query,
            context=str(global_state["df"].to_dict())
        )
        
        logger.info(f"Query processed successfully: {query[:50]}...")
        return {
            "status": "success",
            "query": query,
            "response": response
        }
    
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")