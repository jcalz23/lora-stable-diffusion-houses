import os
import sys
from tqdm import tqdm
from prompts import PROMPT1, PROMPT2, PROMPT3, PROMPT4
sys.path.append('..')
from utils.openai import invoke_image_model
from utils.images import view_image

# Constants
DATA_DIR = '../../data'
IMG_DIR = '../../data/imgs_all'
TEXT_DIR = '../../data/text'
FRONTAL = 'frontal'

def generate_descriptions(num_images=None, view_images=False):
    # Define image list (with frontal in name)
    image_list = [f for f in os.listdir(IMG_DIR) if FRONTAL in f]
    if num_images is not None:
        image_list = image_list[:num_images]
    prompt_list = [PROMPT1, PROMPT2, PROMPT3, PROMPT4]

    for image_fname in tqdm(image_list):
        image_path = os.path.join(IMG_DIR, image_fname)
        image_fname_no_ext = os.path.splitext(image_fname)[0]
        for i, prompt in enumerate(prompt_list):
            text_file_path = os.path.join(TEXT_DIR, f"{image_fname_no_ext}_prompt{i}.txt")
            
            if not os.path.exists(text_file_path):
                description = invoke_image_model(image_path, prompt)
                print(description)

                # Save each description to text dir
                with open(text_file_path, "w") as f:
                    f.write(description)
            elif view_images:
                with open(text_file_path, "r") as f:
                    description = f.read()
                print(f"Description: {description}")
        
        if view_images:
            view_image(image_path, figsize=(6, 4))

if __name__ == "__main__":
    generate_descriptions()
