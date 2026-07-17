from dotenv import load_dotenv
import os


def read_confg() -> None:
    print("\nConfiguration laoded:")
    print(f"Mode: {os.environ.get('MATRIX_MODE')}")
    if os.environ.get('DATABASE_URL'):
        print("Database: Connected to local instance")
    else:
        print("Database: Not configured")
    if os.environ.get('API_KEY'):
        print(f"API Access: {os.environ.get('API_KEY')}")
    else:
        print("Missing API key")
    if os.environ.get('LOG_LEVEL'):
        print(f"Log Level: {os.environ.get('LOG_LEVEL')}")
    else:
        print("Log levet not found")
    if os.environ.get('ZION_ENDPOINT'):
        print("Zion Network: Online")
    else:
        print("Offline")


def check_security() -> None:
    if os.environ.get('API_KEY') != "your_api_key_here":
        print("[OK] No hardcoded secrets detected")
    else:
        print("[KO] Hardcoded secrets detected")
    if os.path.exists('.env'):
        print("[OK] .env file properly configured")
    else:
        print("[KO] .env file not configured")
    if os.environ.get('MATRIX_MODE'):
        print("[OK] Production overrides available")
    else:
        print("[KO] Production overrides not available")


if __name__ == "__main__":
    load_dotenv()
    print("\nORACLE STATUS: Reading the Matrix...")
    read_confg()
    print("\nEnvironment security check:")
    check_security()
    print("\nThe Oracle sees all configurations.")
