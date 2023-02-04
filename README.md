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

1. Start the database docker containers:
  ```
  docker compose up -d
  ```

1. (Optional) From the backend folder, initialize database and run migrations:
  ```
  aerich init -t src.database.config.TORTOISE_ORM
  aerich init-db
  aerich migrate
  aerich upgrade
  ```

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
