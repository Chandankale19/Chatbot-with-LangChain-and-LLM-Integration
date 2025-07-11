# Chatbot-with-LangChain-and-LLM-Integration
The purpose of this project is to develop a production-grade chatbot that enables users to interact with cell-wise data stored in an Excel sheet with columns. The chatbot will use LangChain to process the data and integrate a Large Language Model (LLM) to provide natural language responses based on user queries

# Objectives
Build a chatbot capable of processing and querying cell-wise data from an Excel sheet.
Integrate LangChain for efficient data retrieval and prompt orchestration.
Incorporate an LLM (e.g., OpenAI GPT-4 or equivalent) for natural language understanding and response generation.
Ensure production-grade features: scalability, security, observability, and maintainability.
Provide a user-friendly interface for interacting with the chatbot.
Deploy the application to a cloud platform for accessibility.

# Teacher Registry Chatbot (FastAPI Version)
A production-grade chatbot for querying teacher registry data using LangChain, Google Gemini, and FastAPI with a simple HTML/JavaScript frontend.

## Features
- Upload and process `teacher_registry.xlsx` with columns
- Query data via a web interface or REST API.
- Integrated with Google Gemini for robust query processing.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Chandankale19/Chatbot-with-LangChain-and-LLM-Integration.git
   cd teacher-registry-chatbot
   
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   
3. Set up .env with required keys (see .env template).   


4. Execute app launching script
   ```bash
   bash scripts/start_app.sh
   
5. Access at http://localhost:8000.   

## Tech Stack

1. Programming Language: Python 3.9+
2. Frameworks and Libraries:
3. LangChain: For LLM orchestration and data retrieval.
4. OpenAI API or Google Gemini: For LLM integration.
5. Pandas: For Excel file processing.
6. ChromaDB or FAISS: For vector storage of cell-wise data.
7. HTML,CSS, Javascript for Front end
8. python-dotenv: For environment variable management.

## Usage

1. Open the web interface at http://localhost:8000.

2. Upload teacher_registry.xlsx and submit queries.

3. Example queries:
"List active teachers in GSSS KARERI"
"Who is the lecturer in GSSS BHUNTAR?"
"How many contract employees are active?"

## API endpoints:
1. POST /upload: Upload Excel file.
2. POST /query: Submit a query.

