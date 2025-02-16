# VRL Log Processing Assignment

This assignment processes logs using VRL and Docker. The assignment includes the following files:

- `Dockerfile`
- `docker-compose.yml`
- `input.log`
- `sanity_test.py`
- `expected_output.log`
- `vector.toml`

After running the container, a folder named `logs` will be created where the `output.log` file is generated.

---

## Software Used

- Docker & Docker Compose
- Python 3
- VS Code (for editing)

---

## Running the Container

### Using Your Terminal (WSL2 Ubuntu / Windows Terminal / Command Prompt)

1. Open your terminal and navigate to the project directory.
   ```bash
   cd "path to your directory"

3. **Build the Container:**
   ```bash
   docker-compose build

4. **Start the container in detached mode**
   ```bash
   docker-compose up -d

## **To stop the container**
    docker-compose down

## **To restart the container**
    docker-compose restart

After running the container, a folder named `logs` will be created containing the `output.log` file

# Sanity Test

A Python script `(sanity_test.py)` is provided to validate the generated output.log matches the expected_output.log

# Steps to Run the Sanity Test

1. After the container has run and the logs folder is created, copy the following files into the logs folder:
- `expected_output.log`
- `sanity_test.py`

2. Open your terminal, navigate to the logs folder, and execute:
   
    `cd logs    #replace 'logs' with your actual path`
    ```bash
    python3 sanity_test.py expected_output.log output.log
