import sys
import os
import site

in_venv = sys.prefix != sys.base_prefix

if not in_venv:
    print("MATRIX STATUS: You're still plugged in\n")

    print("Current Python:", sys.executable)
    print("Virtual Environment: None detected\n")

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows\n")

    print("Then run this program again.")

else:
    print("MATRIX STATUS: Welcome to the construct\n")
    print("Current Python:", sys.executable)

    env_path = sys.prefix
    env_name = os.path.basename(env_path)

    print("Virtual Environment:", env_name)
    print("Environment Path:", env_path)
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting"
          "the global system.\n")

    print("Package installation path:")
    for path in site.getsitepackages():
        print(path)
