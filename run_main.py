import subprocess
import sys
import os

def load_env_file(env_file_path):
    with open(env_file_path, 'r') as env_file:
        for line in env_file:
            # Remove whitespace and skip empty or commented lines
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            # Split the line into key and value
            key, _, value = line.partition('=')
            key = key.strip()
            value = value.strip()

            # Set the environment variable
            os.environ[key] = value

def main():
    ENV_FILE = "./dev.env"

    # Load environment variables from the specified file
    load_env_file(ENV_FILE)

    # Ensure debugpy is installed in your virtual environment
    subprocess.run([sys.executable, "-m", "pip", "install", "debugpy"])

    # Command to run the Python script with 'op' and the environment variables
    command = [
      "op", "run", f"--env-file={ENV_FILE}", "--",
      sys.executable,
      "-m", "pip", "install", "debugpy",
      "&&",
      sys.executable,
      "src/main.py"
    ]

    os.environ['DEBUG_SUBPROCESS'] = '1'
    # Run the command
    result = subprocess.run(command, check=True, env=os.environ)

    if result.returncode != 0:
        print("Failed to execute the command.")
        sys.exit(result.returncode)

if __name__ == "__main__":
    main()
