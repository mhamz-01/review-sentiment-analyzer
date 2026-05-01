# ============================================================
# PART 4: Expose FastAPI with ngrok
# ============================================================
# ngrok creates a public URL that tunnels to your local server.
# This lets anyone access your API from the internet.
#
# Steps:
#   1. Get a free token from https://ngrok.com
#   2. Replace YOUR_NGROK_TOKEN below with your actual token
#   3. Run this file: python part4_ngrok.py
#   4. Copy the printed public URL

import threading
import time
import uvicorn
from pyngrok import ngrok
from dotenv import load_dotenv
import os


load_dotenv()

# ---- REPLACE THIS WITH YOUR NGROK AUTH TOKEN ----
NGROK_TOKEN = os.getenv("NGROK_TOKEN")

# ---- IMPORT THE FASTAPI APP ----
from api import app


def run_server():
    """Run uvicorn server in a background thread."""
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="error")


if __name__ == "__main__":
    # Step 1: Kill any existing ngrok tunnels
    ngrok.kill()

    # Step 2: Authenticate with your token
    ngrok.set_auth_token(NGROK_TOKEN)

    # Step 3: Start FastAPI server in background thread
    thread = threading.Thread(target=run_server, daemon=True)
    thread.start()

    # Wait a moment for server to start
    time.sleep(2)

    # Step 4: Open a public tunnel to port 8000
    public_url = ngrok.connect(8000).public_url

    # Step 5: Print the URLs
    print("\n" + "=" * 50)
    print(f"  Public API URL : {public_url}")
    print(f"  Swagger Docs   : {public_url}/docs")
    print("=" * 50)
    print("\nPress CTRL+C to stop.\n")

    # Keep the script running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down...")
        ngrok.kill()