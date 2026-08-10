import subprocess

subprocess.run(["git", "init"], check=True)
subprocess.run(["uv", "sync"], check=True)
subprocess.run(["uv", "run", "pre-commit", "install"], check=True)
