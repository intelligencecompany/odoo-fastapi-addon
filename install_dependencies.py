import subprocess
import sys
import os

def install_requirements():
    try:
        # Path to the requirements.txt file
        requirements_file = os.path.join(os.path.dirname(__file__), 'requirements.txt')
        print(requirements_file)
        # Run the pip install command
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_file])
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies: {e}")

# if __name__ == "__main__":
# install_requirements()
