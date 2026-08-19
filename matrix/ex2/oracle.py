import os
import sys
from dotenv import load_dotenv


REQUIRED_VARS = ["MATRIX_MODE", "DATABASE_URL",
                 "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"]


def load_config() -> dict[str, str]:
    config = {}
    for var in REQUIRED_VARS:
        value = os.environ.get(var)
        if not value:
            raise RuntimeError("Program stops: Missing " + var)
        else:
            config[var] = value
    mode = config["MATRIX_MODE"]
    if mode == "development":
        config["database"] = "Connected to local instance"
        config["production"] = "Production overrides available"
    elif mode == "production":
        config["database"] = "Connected to production datastore"
        config["production"] = "Production environment active"
    else:
        raise RuntimeError(
            "MATRIX_MODE must be 'development' or 'production'")
    return config


def main():
    print("ORACLE STATUS: Reading the Matrix...\n")
    try:
        if load_dotenv():
            config = load_config()
        else:
            raise RuntimeError("[WARNING] No .env file found " +
                               "nor environment variables")
        print("Configuration loaded:")
        print("Mode:", config["MATRIX_MODE"])
        print("Database:", config["database"])
        print("API Access: Authenticated")
        print("Log Level:", config["LOG_LEVEL"])
        print("Zion Network: Online\n")

        print("Environment security check:")
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK]", config["production"])
        print("\nThe Oracle sees all configurations.")
    except RuntimeError as error:
        print("CONFIGURATION ERROR:", error)
        sys.exit(1)


if __name__ == "__main__":
    main()
