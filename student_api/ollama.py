from fastapi import HTTPException
import httpx
from typing import Dict
from .models import Student
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def generate_student_summary(student: Student) -> Dict[str, str]:
    prompt = f"""
    Generate a brief professional summary for this student:
    Name: {student.name}
    Age: {student.age}
    Email: {student.email}
    
    Please focus on creating a concise, formal description.
    """
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "llama3.2", 
                    "prompt": prompt,
                    "stream": False
                }
            )
            logger.info(f"Ollama API response status: {response.status_code}")
            logger.info(f"Ollama API response content: {response.content}")

            response.raise_for_status() 
            response_data = response.json()

            logger.info(f"Parsed response JSON: {response_data}")    # Log parsed JSON data for further inspection
            
            if "response" not in response_data:
                raise ValueError("Unexpected response format from Ollama API: 'response' key missing")
            
            return {"summary": response_data["response"]}
        
        except httpx.HTTPStatusError as http_err:
            error_details = response.json() if response.content else "No content"
            logger.error(f"HTTP error generating summary: {http_err.response.status_code}, Details: {error_details}")
            raise ValueError(f"Error generating summary: {http_err.response.status_code}, Details: {error_details}")
        
        except Exception as e:
            logger.error(f"Unexpected error generating summary: {str(e)}")
            raise HTTPException(
                status_code=500,
                detail=f"Unexpected error generating summary: {str(e)}"
            )
