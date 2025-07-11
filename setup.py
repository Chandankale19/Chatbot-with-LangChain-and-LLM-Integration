from setuptools import setup, find_packages

setup(
    name="teacher-registry-chatbot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "langchain==0.2.14",
        "langchain-google-genai==1.0.10",
        "google-cloud-aiplatform==1.67.1",
        "pandas==2.2.2",
        "openpyxl==3.1.5",
        "chromadb==0.5.5",
        "fastapi==0.115.0",
        "uvicorn==0.30.6",
        "python-multipart==0.0.9",
        "python-dotenv==1.0.1",
        "langsmith==0.1.115",
        "boto3==1.35.24",
        "tenacity==9.0.0",
        "pyyaml==6.0.2",
    ],
    author="Chandan S Kale",
    author_email="Chandankale@1997.com",
    description="A chatbot for querying teacher registry data with FastAPI",
    license="MIT",
    keywords="chatbot langchain google-gemini teacher-registry fastapi",
)

