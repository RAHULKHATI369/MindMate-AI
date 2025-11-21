from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Google Cloud imports
from google.cloud import storage
from google.cloud import aiplatform

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PROJECT_ID = os.getenv("PROJECT_ID")
REGION = os.getenv("REGION")
BUCKET_NAME = os.getenv("BUCKET_NAME")

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize Google Cloud Storage client
storage_client = storage.Client(project=PROJECT_ID)
bucket = storage_client.bucket(BUCKET_NAME)

# Initialize Vertex AI
aiplatform.init(project=PROJECT_ID, location=REGION)

# Example endpoint to check backend
@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "MindMate AI backend is running!"})

# Example endpoint to list files in your bucket
@app.route("/list_files", methods=["GET"])
def list_files():
    blobs = bucket.list_blobs()
    files = [blob.name for blob in blobs]
    return jsonify({"files": files})

# Example endpoint for AI response (replace with Google PaLM API call)
@app.route("/get_response", methods=["POST"])
def get_response():
    data = request.json
    user_message = data.get("message", "")

    # Here you can call Google PaLM/Vertex AI LLM API
    # Example placeholder response
    ai_response = f"Hello! You said: {user_message}"

    return jsonify({"response": ai_response})

if __name__ == "__main__":
    # Run on port 8080 for Cloud Run compatibility
    app.run(host="0.0.0.0", port=8080, debug=True)
