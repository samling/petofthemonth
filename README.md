## Requirements
- python > 3.11
- pyenv (Optional)
- nvm (Optional)
- Docker (Optional)

## Setup

1. Create/activate virtualenv:
    ```
    pyenv activate venv
    ```

1. `pip install -r requirements.txt`

## Running (Development)

1. Start the API server:
  ```
  python main.py
  ```

1. Start the Vue server:
  ```
  npm run dev (local)
  npm run dev -- --host (exposed)
  ```

## Testing

1. Navigate to `http://<ip>:5173` for the VueJS frontend

1. Navigate to `http://<ip>:8000/docs` for the FastAPI application docs page
