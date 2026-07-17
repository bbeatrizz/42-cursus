import sys
import os
import site


def check_env() -> bool:
    if sys.prefix != sys.base_prefix:
        return True
    else:
        return False


def info_env() -> None:
    if not check_env():
        info_not_ev()
    else:
        env_path: str = os.environ.get('VIRTUAL_ENV', "None detected")
        print("\nMATRIX STATUS: Welcome to the construct")
        print(f"\nCurrent Python:{sys.executable}")
        print(f"Virtual Environment: {env_path}")
        print(f"Environment Path: {os.path.basename(env_path)}")
        print("""\nSUCCESS: You're in an isolated environment!
Safe to install packages without affecting
the global system.""")
        print(f"""\nPackage installation path:
{site.getsitepackages()[0]}""")


def info_not_ev() -> None:
    print("\nMATRIX STATUS: You're still plugged in")
    print(f"\nCurrent Python: {sys.executable}")
    print("Virtual Environment: "
          f"{os.environ.get('VIRTUAL_ENV')} detected")
    print("""\nWARNING: You're in the global environment!
The machines can see everything you install.""")
    print("""\nTo enter the construct, run:
python3 -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env\\Scripts\\activate # On Windows""")
    print("\nThen run this program again.")


if __name__ == "__main__":
    info_env()
