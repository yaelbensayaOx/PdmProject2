import requests
import numpy as np
import sys

def check_versions():
    # Desired versions
    target_requests = "2.25.1"
    target_numpy = "1.20.3"

    print(f"--- Environment Check ---")
    print(f"Python version: {sys.version.split()[0]}")
    print(f"Requests version: {requests.__version__} (Target: {target_requests})")
    print(f"NumPy version: {np.__version__} (Target: {target_numpy})")
    print("-" * 25)

    # Simple logic using NumPy
    # Creating a 3x3 identity matrix
    matrix = np.eye(3)
    print(f"\nNumPy Test (Identity Matrix):\n{matrix}")

    # Simple logic using Requests
    # Fetching a sample status code
    try:
        response = requests.get("https://api.github.com", timeout=5)
        print(f"\nRequests Test: Connected to GitHub API (Status: {response.status_code})")
    except Exception as e:
        print(f"\nRequests Test: Failed to connect. Error: {e}")

if __name__ == "__main__":
    check_versions()
