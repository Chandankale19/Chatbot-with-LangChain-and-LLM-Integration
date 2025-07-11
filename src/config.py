import os
from dotenv import load_dotenv
import logging

load_dotenv()

# Environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")

# Validate environment variables
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is not set in .env file")
if not LANGCHAIN_API_KEY:
    logging.warning("LANGCHAIN_API_KEY is not set; LangSmith tracing disabled")

# LangSmith tracing
os.environ["LANGCHAIN_TRACING_V2"] = "false"
os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY or ""

# Project constants
DATA_PATH = "data/teacher_registry.xlsx"
EXPECTED_COLUMNS = [
    "School_Code", "School_Name", "Employee_Name", "teacher_Code",
    "Designation", "Employee_Type", "Is_Active?"
]

