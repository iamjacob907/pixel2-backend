from flask import Flask, request, jsonify
import replicate
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to access backend

# Load Replicate API key from environment variable
os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt")
    image_url = data.get("image_url")  # Optional

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        output = replicate.run(
            "your-username/your-model-name:version-id",  # Replace this with the correct model
            input={
                "prompt": prompt,
                "image": image_url
            }
        )
        return jsonify({"video_url": output})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
