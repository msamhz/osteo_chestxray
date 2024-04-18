import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define the directory structure for src/ based on the first image
src_structure = [
    f"app/__init__.py",
    f"data_prep/__init__.py",
    f"model/__init__.py",
    f"tests/__init__.py",
    f"training/__init__.py",
    f"utils/__init__.py",
    f"utils/constants.py",
    f"main.py",
]

# Define the directory structure for the main project based on the second image
project_structure = [
    ".git",
    "assets/.gitkeep",
    "conf/cfg.yaml",
    "conf/cfg_tuning.yaml",
    "data/.gitkeep",
    "docker/.gitkeep",
    "docs/.gitkeep",
    "models/.gitkeep",
    "notebooks/trials.ipynb",
    "scripts/bat_scripts",
    "scripts/docker_tar",
    "src",
    ".dockerignore",
    ".gitignore",
    ".gitlab-ci",
    ".isort.cfg",
    ".pre-commit-config.yaml",
    ".pylintrc",
    "docker-compose-cpu.yaml",
    "docker-compose-gpu.yaml",
    "requirements.txt",
    "README.md",
]

# Create src/ directory structure
for path in src_structure:
    full_path = Path(f"src/{path}")
    os.makedirs(full_path.parent, exist_ok=True)
    full_path.touch(exist_ok=True)
    logging.info(f"Created {full_path}")

# Create the main project structure
for path in project_structure:
    if '.' in path or '-' in path:  # Checks if it's a file or specific directory like '.git'
        if not os.path.exists(path):
            if path.endswith('/'):  # It's a directory
                os.makedirs(path, exist_ok=True)
                logging.info(f"Created directory: {path}")
            else:  # It's a file
                Path(path).touch()
                logging.info(f"Created file: {path}")
    else:  # It's a regular directory
        os.makedirs(path, exist_ok=True)
        logging.info(f"Created directory: {path}")
