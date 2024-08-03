import requests
import os
import random
from constants import *

def collect_images():
    # Image Ids
    image_ids = [f"{i}_frontal.jpg" for i in range(100, 440)]
    image_ids = random.sample(image_ids, min(NUM_IMAGES, len(image_ids)))

    for image_id in image_ids:
        # Save the image to local
        image_url = f"{GITHUB_IMG_DIR}/{image_id}"
        response = requests.get(image_url)
        if response.status_code == 200:
            # Save the image
            os.makedirs(IMG_DIR, exist_ok=True)
            with open(f"{IMG_DIR}/{image_id}", "wb") as file:
                file.write(response.content)
        else:
            print(f"Failed to download image: {image_id}. Status code: {response.status_code}")

if __name__ == "__main__":
    collect_images()
