# Infinitex

A simple project to test infinite scroll using HTMX.

## Project Setup

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/julioh1203/infinitex.git
    cd infinitex
    ```

### Running the Project

1. Run the development server:

   ```sh
        docker compose -f docker-compose.yaml up --build
   ```

2. Import the books to the database:

    ```sh
    docker compose -f docker-compose.yaml exec -it web python manage.py importbooks
    ```

3. Open your browser and go to `http://0.0.0.0:8000/`.
