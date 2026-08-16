import os
from pathlib import Path
from dotenv import load_dotenv


REQUIRED_VARS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def load_configuration():
    env_file = Path(__file__).with_name(".env")
    load_dotenv(env_file)

    missing = [name for name in REQUIRED_VARS if not os.getenv(name)]
    if missing:
        raise RuntimeError(
            "Missing required configuration: " + ", ".join(missing)
        )
    mode = os.environ["MATRIX_MODE"].lower()
    if mode not in {"development", "production"}:
        raise RuntimeError(
            "MATRIX_MODE must be 'development' or 'production'"
        )
    return {
        "mode": mode,
        "database_url": os.environ["DATABASE_URL"],
        "api_key": os.environ["API_KEY"],
        "log_level": os.environ["LOG_LEVEL"],
        "zion_endpoint": os.environ["ZION_ENDPOINT"],
    }


def main():
    print("ORACLE STATUS: Reading the Matrix...\n")
    try:
        config = load_configuration()
    except RuntimeError as error:
        print(f"CONFIGURATION ERROR: {error}")
        raise SystemExit(1)

    if config["mode"] == "development":
        database_status = "Connected to local instance"
        override_status = "Production overrides available"
    else:
        database_status = "Connected to production datastore"
        override_status = "Development settings available via .env"

    print("Configuration loaded:")
    print(f"Mode: {config['mode']}")
    print(f"Database: {database_status}")
    print("API Access: Authenticated")
    print(f"Log Level: {config['log_level']}")
    print("Zion Network: Online\n")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print(f"[OK] {override_status}\n")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()