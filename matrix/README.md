# Description
This project is about virtual environment and package management.
Unlike Born2BeRoot to create a virtual machine, this project focusing on the virtual environment to execute a program.

Known container or package management tool: Conda / Anaconda / Docker

## Project Structure
- ex0: **isolated environment** - how to detect current environment and change to virtual environment
- ex1: **program dependency & package management** - build a data analysis tool that requires external libraries.
- ex2: secure configuration system


# EX2: Oracle

A Python configuration management project that demonstrates how to safely handle application settings, API keys, database connection strings, and environment-specific configuration using **environment variables** and **python-dotenv**.

## Overview

The Oracle has access to the Matrix's configuration. In a real application, sensitive configuration such as database credentials and API keys should **not** be hardcoded into source code.

This project demonstrates how to:

* Load configuration from environment variables.
* Use a `.env` file for local development.
* Support separate development and production configurations.
* Validate required configuration variables.
* Handle missing or invalid configuration safely.
* Keep secrets out of version control.

## Project Files

```text
oracle.py
.env
.env.example
.gitignore
requirements.txt
README.md
```

### `oracle.py`

The main Python program. It uses `python-dotenv` to load settings from `.env` and then reads the configuration through `os.environ`.

It validates all required configuration variables and checks that `MATRIX_MODE` is either `development` or `production`.

### `.env`

Contains local development configuration.

**This file should never be committed to Git**, because it may contain sensitive information such as API keys or database credentials.

### `.env.example`

A safe template showing which configuration variables are required.

It should contain placeholders rather than real secrets.

### `.gitignore`

Prevents `.env` and other generated Python files from being committed to version control.

### `requirements.txt`

Contains the project's Python dependency:

```text
python-dotenv>=1.0,<2
```

## Configuration

The application requires five environment variables:

| Variable        | Description                                            |
| --------------- | ------------------------------------------------------ |
| `MATRIX_MODE`   | Application environment: `development` or `production` |
| `DATABASE_URL`  | Database/storage connection string                     |
| `API_KEY`       | Secret key used for external services                  |
| `LOG_LEVEL`     | Logging verbosity such as `DEBUG` or `INFO`            |
| `ZION_ENDPOINT` | URL used to connect to the Zion network                |

## Development Configuration

For local development, create a `.env` file:

```env
MATRIX_MODE=development
DATABASE_URL=sqlite:///./matrix-dev.db
API_KEY=development-placeholder-key
LOG_LEVEL=DEBUG
ZION_ENDPOINT=https://zion.example.test/network
```

Install the dependency:

```bash
python -m pip install -r requirements.txt
```

Then run:

```bash
python oracle.py
```

Expected output:

```text
ORACLE STATUS: Reading the Matrix...
Configuration loaded:
Mode: development
Database: Connected to local instance
API Access: Authenticated
Log Level: DEBUG
Zion Network: Online
Environment security check:
[OK] No hardcoded secrets detected
[OK] .env file properly configured
[OK] Production overrides available
The Oracle sees all configurations.
```

## Production Configuration

Production settings should normally be supplied by the deployment environment rather than committing a production `.env` file.

For example:

```bash
MATRIX_MODE=production \
DATABASE_URL="postgresql://..." \
API_KEY="production-secret" \
LOG_LEVEL=INFO \
ZION_ENDPOINT="https://zion.example.com/network" \
python oracle.py
```

The application will use these environment variables instead of the development values in `.env`.

The output will show the environment difference:

```text
Configuration loaded:
Mode: production
Database: Connected to production datastore
API Access: Authenticated
Log Level: INFO
Zion Network: Online
```

## How Configuration Loading Works

The program uses `python-dotenv`:

```python
from dotenv import load_dotenv

load_dotenv()
```

This loads variables from `.env` into the process environment.

The program then accesses them using Python's standard `os` module:

```python
import os

mode = os.environ["MATRIX_MODE"]
api_key = os.environ["API_KEY"]
```

This keeps configuration separate from the application code.

## Error Handling

The program checks that all required variables exist.

If configuration is missing, it reports the problem instead of continuing with incomplete settings:

```text
CONFIGURATION ERROR: Missing required configuration: API_KEY
```

It also validates `MATRIX_MODE`.

Only these values are accepted:

```text
development
production
```

An invalid value produces a configuration error.

## Security

### Why `.env` is ignored

The `.env` file may contain secrets such as:

* API keys
* Database passwords
* Database connection strings
* Private service endpoints
* Other deployment credentials

Committing these values to Git could expose them to other developers or, if the repository is public, to the entire internet.

For that reason, `.gitignore` contains:

```gitignore
.env
.env.*
!.env.example
```

This prevents `.env` from being tracked while allowing `.env.example` to be committed.

### Never hardcode secrets

Avoid code like:

```python
API_KEY = "my-real-secret-key"
```

Instead, use:

```python
API_KEY = os.environ["API_KEY"]
```

This allows the secret to be supplied securely by the environment.

## Development vs Production

The project demonstrates environment-specific behavior through `MATRIX_MODE`.

### Development

* Uses local database configuration.
* Uses `DEBUG` logging.
* Loads convenient development values from `.env`.
* Suitable for local testing.

### Production

* Uses production environment variables.
* Uses a production database connection.
* Can use a less verbose logging level such as `INFO`.
* Secrets can be supplied by the deployment environment.
* No production secrets need to be stored in the source repository.

## Requirements

* Python 3.x
* `python-dotenv`

Install dependencies with:

```bash
python -m pip install -r requirements.txt
```

## Running the Program

Development:

```bash
python oracle.py
```

Production example:

```bash
MATRIX_MODE=production \
DATABASE_URL="your-production-database-url" \
API_KEY="your-production-api-key" \
LOG_LEVEL=INFO \
ZION_ENDPOINT="https://your-production-endpoint" \
python oracle.py
```

## Learning Goals

This project demonstrates several important configuration-management practices:

1. **Separate configuration from source code.**
2. **Use environment variables for deployment-specific settings.**
3. **Use `.env` for convenient local development.**
4. **Never commit real secrets to version control.**
5. **Validate configuration when the application starts.**
6. **Allow production environments to override development settings.**
7. **Use `python-dotenv` instead of implementing a custom `.env` parser.**

## Conclusion

The Oracle configuration system provides a simple example of secure configuration management in Python.

The core principle is:

> **Code belongs in version control. Secrets belong in the environment.**

The Oracle sees all configurations — but the secrets don't need to be committed to the Matrix.
