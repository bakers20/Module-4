import os
import subprocess
import platform

# Step 1: Create the project directory
project_dir = os.path.expanduser("~/djangogirls")  # Adjust if you need a different directory
if not os.path.exists(project_dir):
    os.mkdir(project_dir)
print(f"Created directory: {project_dir}")

# Step 2: Create the virtual environment
venv_dir = os.path.join(project_dir, "myvenv")
python_command = "python3" if platform.system() != "Windows" else "python"

try:
    print(f"Creating virtual environment in {venv_dir}...")
    subprocess.run([python_command, "-m", "venv", venv_dir], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error creating virtual environment: {e}")
    exit(1)

# Step 3: Activate the virtual environment
if platform.system() == "Windows":
    activate_command = os.path.join(venv_dir, "Scripts", "activate.bat")
else:
    activate_command = f"source {os.path.join(venv_dir, 'bin', 'activate')}"

print(f"Run this command to activate your virtual environment:\n{activate_command}")

# Step 4: Create requirements.txt and add Django
requirements_file = os.path.join(project_dir, "requirements.txt")
with open(requirements_file, "w") as f:
    f.write("Django~=4.2.11\n")

print(f"Created requirements.txt at {requirements_file}")

# Step 5: Install Django using requirements.txt
try:
    print("Installing Django...")
    subprocess.run([os.path.join(venv_dir, "bin", "pip") if platform.system() != "Windows" else os.path.join(venv_dir, "Scripts", "pip"), 
                    "install", "-r", requirements_file], check=True)
    print("Django successfully installed!")
except subprocess.CalledProcessError as e:
    print(f"Error installing Django: {e}")
