import os
import subprocess
import sys

def create_venv():
    print("Creating a virtual environment...")
    subprocess.check_call([sys.executable, "-m", "venv", "venv"])

def install_dependencies():
    print("Installing dependencies...")
    subprocess.check_call(["venv/bin/pip", "install", "-U", "setuptools==69.5.1", "wheel"])
    subprocess.check_call(["venv/bin/pip", "install", "-r", "requirements.txt"])
    print("Dependencies installed successfully.")

def download_assets():
    print("Downloading models for offline use...")
    os.makedirs("models", exist_ok=True)
    # Example URL for model - replace with the actual Hugging Face download URL
    subprocess.check_call(["curl", "-o", "models/model.bin", "https://example.com/model.bin"])
    print("Models downloaded.")

def main():
    print("Starting one-click setup...")
    create_venv()
    install_dependencies()
    download_assets()
    print("Setup complete! You can now run the project.")

if __name__ == "__main__":
    main()
