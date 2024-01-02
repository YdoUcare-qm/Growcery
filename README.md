# Growcery App

Welcome to Growcery, your go-to app for managing grocery lists and more!

## Setup

### Python Environment

1. **Clone the repository:**
    ```bash
    git clone https://github.com/YdoUcare-qm/Growcery.git
    cd Growcery
    ```

2. **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - On Unix or MacOS:
        ```bash
        source venv/bin/activate
        ```

4. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Start the Server

Run the following command to start the server:
```bash
python main.py
```
# Celery Configuration for Growcery App

## Running Celery Worker

1. Open a terminal and navigate to your project root directory.

2. Run the following command to start Celery Worker:

    ```bash
    celery -A main:celery_app worker --loglevel=info
    ```

   This command initializes the Celery worker, allowing it to process tasks in the background.

## Running Celery Beat (Periodic Tasks)

1. Open another terminal window/tab and navigate to your project root directory.

2. Run the following command to start Celery Beat:

    ```bash
    celery -A main:celery_app beat --loglevel=info
    ```

   This command starts Celery Beat, which is responsible for scheduling and triggering periodic tasks.




