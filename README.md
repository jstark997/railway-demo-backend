# Railway Demo Backend (FastAPI)

A simple FastAPI backend for testing Railway deployment.

## Endpoints

- `GET /` - Root endpoint
- `GET /api/status` - Status check
- `POST /api/echo` - Echo a message
- `GET /api/items` - Get list of items

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## Railway Deployment

This app is configured to deploy automatically to Railway. The `railway.json` file contains the deployment configuration.

Make sure to update the CORS settings in `main.py` with your frontend URL after deployment.
