import requests
from pathlib import Path

TOKEN = "your_taken_here"
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"

headers = {"Authorization": f"Bearer {TOKEN}"}

def image_to_text(image_path: str) -> str:
    image_bytes = Path(image_path).read_bytes()
    response = requests.post(API_URL, headers=headers, data=image_bytes)
    
    if response.status_code != 200:
        raise Exception(f"Error {response.status_code}: {response.text}")
    
    result = response.json()
    return result[0]["generated_text"]

caption = image_to_text("lemoncake.webp")
print("Caption:", caption)