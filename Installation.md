 Introduction
Objective: Install and run the SF3D project offline while resolving any issues encountered during the process.
Overview: Summarize what SF3D is and its capabilities. Reference key features like 3D mesh reconstruction, UV unwrapping, and illumination disentanglement.
2. System Prerequisites
List the system requirements:

OS: Linux/Mac/Windows (experimental)
Python: ≥ 3.8
CUDA/MPS/CPU requirements
Visual Studio (Windows experimental)
3. Installation Process
Step 1: Clone the Repository
Document how to clone the repository:

bash
Copy code
git clone https://github.com/Stability-AI/stable-fast-3d.git
cd stable-fast-3d
Step 2: Set Up the Environment
Create a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -U setuptools==69.5.1
pip install wheel
pip install -r requirements.txt
Optional: Install demo dependencies:

bash
Copy code
pip install -r requirements-demo.txt
Step 3: Handle GPU/CPU Requirements
For CUDA-based systems, install the appropriate version of PyTorch:
bash
Copy code
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
For MPS (Mac Silicon):
Install the OpenMP runtime (link in README).
Use PYTORCH_ENABLE_MPS_FALLBACK=1.
Step 4: Offline Model Access
Explain how to use Hugging Face's huggingface-cli to download the model and ensure offline functionality:

Log in and request access on Hugging Face.
Generate a token and log in:
bash
Copy code
huggingface-cli login
Step 5: Run the Code
For single-image inference:
bash
Copy code
python run.py demo_files/examples/chair1.png --output-dir output/
For the Gradio demo:
bash
Copy code
python gradio_app.py
4. Challenges and Solutions
Problem 1: PyTorch Version Conflict
Issue: The CUDA version of PyTorch was not compatible with my system.
Solution: Verified system CUDA version and installed the corresponding PyTorch.
Problem 2: Missing Dependencies
Issue: setuptools and wheel versions were outdated.
Solution: Updated them explicitly:
bash
Copy code
pip install -U setuptools==69.5.1
pip install wheel
Problem 3: Hugging Face Access
Issue: Could not download the model initially.
Solution: Created a token with read permissions and logged in using huggingface-cli.
Problem 4: Offline Functionality
Issue: The code fetched assets online during runtime.
Solution: Pre-downloaded required models and modified the script to use local paths.
Problem 5: High Memory Usage
Issue: Gradio app crashed on low-memory systems.
Solution: Reduced texture resolution using --texture-resolution flag.
5. Lessons Learned
Importance of matching system configurations with library requirements.
Managing offline dependencies proactively avoids runtime errors.
Regularly update dependencies like PyTorch and setuptools for compatibility.
6. Recommendations
Include a pre-downloaded assets folder in the repository for offline usage.
Add a check in the code for system compatibility (e.g., CUDA/MPS/CPU).
