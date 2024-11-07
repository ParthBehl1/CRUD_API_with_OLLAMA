# Student Management API

A **FastAPI-based RESTful API** for managing student records, allowing users to create, retrieve, update, and delete (CRUD) student profiles. This API includes AI-powered summary generation using **Ollama's Llama language model**, which produces professional summaries for each student profile.

## Features

- **Student CRUD Operations**: Create, view, update, and delete student profiles.
- **AI-Powered Summary**: Generate concise, formal summaries of student information using the Llama model.
- **Thread-Safe Storage**: The API uses an in-memory data store for handling student data safely across concurrent requests.

## Tech Stack

- **FastAPI** for the RESTful API framework
- **Pydantic** for data validation
- **httpx** for async HTTP requests to the AI model
- **Ollama Llama model** for generating professional summaries

---

## Prerequisites

- **Python 3.8+**
- **Ollama** for summary generation, with the **Llama3.2 model** installed.

## Setup Instructions

1. **Clone the Repository**:

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Install Ollama**:
    Follow instructions at [Ollama GitHub](https://github.com/ollama/ollama) to install Ollama.

4. **Download the Llama Model**:
    ```bash
    ollama pull llama3.2
    ```

5. **Run the API**:
    ```bash
    python -m student_api.main
    ```

    The API will start at `http://localhost:8000`. Access interactive documentation at `http://localhost:8000/docs`.

---

## API Endpoints

- **Create Student**: `POST /students`
- **Retrieve All Students**: `GET /students`
- **Retrieve Student by ID**: `GET /students/{student_id}`
- **Update Student by ID**: `PUT /students/{student_id}`
- **Delete Student by ID**: `DELETE /students/{student_id}`
- **Generate Student Summary**: `GET /students/{student_id}/summary`

---

## Testing the API

### 1. Create a Student

```bash
curl -X POST http://localhost:8000/students \
  -H "Content-Type: application/json" \
  -d '{"name": "parth behl", "age": 21, "email": "parth@example.com"}'
```

### 2. Get All Students

```bash
curl http://localhost:8000/students
```

### 3. Get Student by ID

```bash
curl http://localhost:8000/students/1
```

### 4. Update Student by ID

```bash
curl -X PUT http://localhost:8000/students/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "parth behl", "age": 22, "email": "parth.behl@example.com"}'
```

### 5. Generate Student Summary

```bash
curl http://localhost:8000/students/1/summary
```

### 6. Delete Student by ID

```bash
curl -X DELETE http://localhost:8000/students/1
```

---

## Project Structure

```plaintext
student_api/
├── __init__.py           # Package init
├── api.py                # FastAPI routes and dependencies
├── main.py               # Entry point to start the FastAPI server
├── models.py             # Pydantic models for data validation
├── storage.py            # In-memory storage logic
├── ollama.py             # AI summary generation logic
└── requirements.txt      # Python dependencies
README.md                 # Project README
```

---

## Troubleshooting

If the AI summary generation fails, ensure:
- **Ollama is installed and running**, with `llama3.2` model accessible locally.
- **Correct endpoint**: The Ollama model should be available at `http://localhost:11434/api/generate`.

### Common Errors

- **500 Error on Summary Generation**: Check Ollama installation or model download.
- **Missing Dependencies**: Reinstall packages with `pip install -r requirements.txt`.

---
