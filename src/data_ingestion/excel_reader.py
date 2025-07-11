import pandas as pd
import logging
from src.utils.logger import setup_logger
from src.config import EXPECTED_COLUMNS

logger = setup_logger()

def read_excel(file_path):
    """
    Read and validate Excel file for required columns.
    
    Args:
        file_path (str or file-like): Path to Excel file or uploaded file object.
    
    Returns:
        pd.DataFrame: Validated DataFrame with expected columns.
    
    Raises:
        ValueError: If file is empty or missing required columns.
        Exception: For other file reading errors.
    """
    try:
        # Handle both file path and file-like objects
        if isinstance(file_path, str):
            df = pd.read_excel(file_path, usecols=EXPECTED_COLUMNS)
        else:
            df = pd.read_excel(file_path, usecols=EXPECTED_COLUMNS)
        
        if df.empty:
            logger.error("Excel file is empty")
            raise ValueError("Excel file is empty")
        
        if not all(col in df.columns for col in EXPECTED_COLUMNS):
            missing_cols = [col for col in EXPECTED_COLUMNS if col not in df.columns]
            logger.error(f"Missing required columns: {missing_cols}")
            raise ValueError(f"Missing required columns: {missing_cols}")
        
        logger.info(f"Successfully read Excel file with {len(df)} rows")
        return df
    
    except ValueError as ve:
        raise ve
    except Exception as e:
        logger.error(f"Failed to read Excel file: {str(e)}")
        raise Exception(f"Failed to read Excel file: {str(e)}")