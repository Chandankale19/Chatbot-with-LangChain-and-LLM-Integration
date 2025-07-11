# API Documentation

## Endpoints

### `GET /`
- **Description**: Serves the main HTML page for the chatbot interface.
- **Response**: `200 OK` with HTML content.

### `POST /upload`
- **Description**: Uploads and processes an Excel file (`teacher_registry.xlsx`).
- **Request**:
  - Content-Type: `multipart/form-data`
  - Body: `file` (Excel file, .xlsx)
- **Responses**:
  - `200 OK`: `{ "status": "success", "message": "File processed successfully", "preview": [...] }`
  - `400 Bad Request`: Invalid file type or validation error.
  - `500 Internal Server Error`: Processing error.

### `POST /query`
- **Description**: Processes a user query.
- **Request**:
  - Content-Type: `application/json`
  - Body: `{ "query": "List active teachers in GSSS KARERI" }`
- **Responses**:
  - `200 OK`: `{ "status": "success", "query": "...", "response": "..." }`
  - `400 Bad Request`: No file uploaded or invalid query.
  - `500 Internal Server Error`: Processing error.

## Components
- **Excel Reader**: Validates and reads Excel files.
- **Vector Store**: Creates Chroma vectors for data retrieval.
- **LLM Integration**: Interfaces with Google Gemini.
- **LangChain Core**: Manages conversational retrieval.
- **Query Processor**: Formats queries with prompts.
- **FastAPI**: Provides RESTful endpoints and serves the HTML frontend.

## Example Usage
```bash
# Upload file
curl -X POST http://localhost:8000/upload -F "file=@teacher_registry.xlsx"

# Submit query
curl -X POST http://localhost:8000/query -H "Content-Type: application/json" -d '{"query":"List active teachers in GSSS KARERI"}'