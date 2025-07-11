<<<<<<< HEAD
=======
# Chatbot-with-LangChain-and-LLM-Integration
The purpose of this project is to develop a production-grade chatbot that enables users to interact with cell-wise data stored in an Excel sheet with columns. The chatbot will use LangChain to process the data and integrate a Large Language Model (LLM) to provide natural language responses based on user queries

# Objectives
Build a chatbot capable of processing and querying cell-wise data from an Excel sheet.
Integrate LangChain for efficient data retrieval and prompt orchestration.
Incorporate an LLM (e.g., OpenAI GPT-4 or equivalent) for natural language understanding and response generation.
Ensure production-grade features: scalability, security, observability, and maintainability.
Provide a user-friendly interface for interacting with the chatbot.
Deploy the application to a cloud platform for accessibility.

>>>>>>> 474fb79fba4cb132ebb446c626ae91b032f88e14
# Teacher Registry Chatbot (FastAPI Version)

A production-grade chatbot for querying teacher registry data using LangChain, Google Gemini, and FastAPI with a simple HTML/JavaScript frontend.

## Features
<<<<<<< HEAD
- Upload and process `teacher_registry.xlsx` with columns: `School_Code`, `School_Name`, `Employee_Name`, `teacher_Code`, `Designation`, `Employee_Type`, `Is_Active?`.
- Query data via a web interface or REST API (e.g., "List active teachers in GSSS KARERI").
- Integrated with Google Gemini for robust query processing.
- Deployable on AWS EC2 or other platforms supporting FastAPI.
- Observability with AWS CloudWatch and LangSmith.

=======
- Upload and process `teacher_registry.xlsx` with columns
- Query data via a web interface or REST API.
- Integrated with Google Gemini for robust query processing.
- 
>>>>>>> 474fb79fba4cb132ebb446c626ae91b032f88e14
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
<<<<<<< HEAD
POST /upload: Upload Excel file.
POST /query: Submit a query.
=======
1. POST /upload: Upload Excel file.
2. POST /query: Submit a query.
>>>>>>> 474fb79fba4cb132ebb446c626ae91b032f88e14
