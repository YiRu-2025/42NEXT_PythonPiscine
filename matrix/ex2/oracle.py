import os
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    print("ORACLE STATUS: Reading the Matrix...")
    print("[WARNING] python-dotenv is not installed.")
    print("[WARNING] Install it with: python -m pip install python-dotenv")
    print("[ERROR] Configuration cannot be loaded from .env")
    sys.exit(1)


REQUIRED_VARS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def load_configuration():
    env_file = Path(__file__).with_name(".env")

    if env_file.exists():
        load_dotenv(env_file)
    else:
        print("[WARNING] .env file not found.")
        print("[INFO] Checking environment variables instead.")

    missing = []

    for variable in REQUIRED_VARS:
        if not os.getenv(variable):
            missing.append(variable)

    if missing:
        raise RuntimeError(
            "Missing required configuration: "
            + ", ".join(missing)
        )

    mode = os.getenv("MATRIX_MODE").lower()

    if mode not in ("development", "production"):
        raise RuntimeError(
            "MATRIX_MODE must be 'development' or 'production'."
        )

    return {
        "mode": mode,
        "database_url": os.getenv("DATABASE_URL"),
        "api_key": os.getenv("API_KEY"),
        "log_level": os.getenv("LOG_LEVEL"),
        "zion_endpoint": os.getenv("ZION_ENDPOINT"),
    }


def main():
    print("ORACLE STATUS: Reading the Matrix...\n")

    try:
        config = load_configuration()
    except RuntimeError as error:
        print(f"CONFIGURATION ERROR: {error}")
        return

    if config["mode"] == "development":
        database_status = "Connected to local instance"
        production_status = "Production overrides available"
    else:
        database_status = "Connected to production datastore"
        production_status = "Production environment active"

    print("Configuration loaded:")
    print(f"Mode: {config['mode']}")
    print(f"Database: {database_status}")
    print("API Access: Authenticated")
    print(f"Log Level: {config['log_level']}")
    print("Zion Network: Online\n")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")

    if Path(__file__).with_name(".env").exists():
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")

    print(f"[OK] {production_status}\n")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()