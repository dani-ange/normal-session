import json
from huggingface_hub import Repository, login
import os
from shutil import copytree, rmtree
import subprocess

    # --- Hugging Face setup ---
    # Authenticate using HF_TOKEN from environment variable.
hf_token = os.environ["HF_TOKEN"]
repo_id = "danielle2003/tp1"  # ⚠️ REPLACE with your actual repo ID

if not hf_token:
    raise EnvironmentError("❌ Please set the HF_TOKEN environment variable.")

login(token=hf_token)

    # --- Prepare local repo ---
    # Clones the Hugging Face repo locally and clears any previous clone.
repo_dir = "./hf_repo"
if os.path.exists(repo_dir):
    rmtree(repo_dir)

repo = Repository(local_dir=repo_dir, clone_from=repo_id, use_auth_token=hf_token)

    # --- Copy model files ---
    # Copies trained model files into the local repo.
dest = os.path.join(repo_dir, "mnist_model")
if os.path.exists(dest):
    rmtree(dest)

copytree("./model", dest)

    # --- Git config ---
    # Set global Git identity (required for automated commits).
subprocess.run(['git', 'config', '--global', 'user.email', 'danielle@example.com'], check=True)
subprocess.run(['git', 'config', '--global', 'user.name', 'Danielle'], check=True)

    # --- Commit and push ---
    # Stages, commits, and pushes model to Hugging Face Hub.
repo.git_add()
repo.git_commit("🚀 Deploying model after successful evaluation")
try:
    repo.git_push()
    print("✅ Model deployed successfully to Hugging Face Hub!")
except Exception as e:
    print(f"❌ Deployment failed: {e}")


