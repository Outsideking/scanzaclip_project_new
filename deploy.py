import os
import subprocess
import json

def auto_deploy(instance_path: str, master_api_key: str, port: int):
    config_path = os.path.join(instance_path, "config.json")
    with open(config_path) as f:
        config = json.load(f)
    
    if config.get("owner") != master_api_key:
        raise PermissionError("Master API Key mismatch!")
    
    subprocess.run(["pip", "install", "-r", "../requirements.txt"], cwd=instance_path)
    subprocess.Popen(["uvicorn", "run_api:app", "--host", "0.0.0.0", f"--port={port}"], cwd=instance_path)
    
    print(f"Deployment complete: {instance_path} on port {port}")

# Deploy
auto_deploy("instances/public_a", "SUPERSECRET_RUFIO_KEY", 8001)
auto_deploy("instances/public_b", "SUPERSECRET_RUFIO_KEY", 8002)
