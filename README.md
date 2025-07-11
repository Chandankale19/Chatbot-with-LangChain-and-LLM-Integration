# Teacher Registry Chatbot (FastAPI Version)

A production-grade chatbot for querying teacher registry data using LangChain, Google Gemini, and FastAPI with a simple HTML/JavaScript frontend.

## Features
- Upload and process `teacher_registry.xlsx` with columns: `School_Code`, `School_Name`, `Employee_Name`, `teacher_Code`, `Designation`, `Employee_Type`, `Is_Active?`.
- Query data via a web interface or REST API (e.g., "List active teachers in GSSS KARERI").
- Integrated with Google Gemini for robust query processing.
- Deployable on AWS EC2 or other platforms supporting FastAPI.
- Observability with AWS CloudWatch and LangSmith.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/teacher-registry-chatbot.git
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

## Usage

1. Open the web interface at http://localhost:8000.

2. Upload teacher_registry.xlsx and submit queries.

3. Example queries:
"List active teachers in GSSS KARERI"
"Who is the lecturer in GSSS BHUNTAR?"
"How many contract employees are active?"

## API endpoints:
POST /upload: Upload Excel file.
POST /query: Submit a query.
