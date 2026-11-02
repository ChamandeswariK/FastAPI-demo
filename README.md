
# FastAPI Demo

A simple FastAPI application built with Python and managed using `uv`.

## Project Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd FastAPI-demo/src
```

### 2. Create a Virtual Environment

```bash
uv venv
```

Activate the virtual environment.

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

Install the required packages using `requirements.txt`.

```bash
uv pip install -r requirements.txt
```

Alternatively, install dependencies directly using `uv`:

```bash
uv sync
```

### 4. Navigate to the Source Directory

```bash
cd src
```

### 5. Run the FastAPI Application

```bash
uvicorn main:app --reload
```

The application will start at:

http://127.0.0.1:8000

## API Documentation

FastAPI provides interactive API documentation.

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic
- uv

## Project Structure

```text
FastAPI-demo/
├── pyproject.toml
├── requirements.txt
├── README.md
├── .python-version
├── .venv/
└── src/
    └── main.py
```

## Development

Run the application with auto-reload enabled:

```bash
uvicorn main:app --reload
```

## Dependencies

Project dependencies are managed in `pyproject.toml` and exported to `requirements.txt`.

To regenerate `requirements.txt`:

```bash
uv export --format requirements-txt --no-hashes --output-file requirements.txt
```

## License

This project is intended for learning and development purposes.
