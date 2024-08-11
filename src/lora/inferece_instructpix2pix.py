import PIL
from PIL import Image
import requests
import torch
from diffusers import StableDiffusionInstructPix2PixPipeline, EulerAncestralDiscreteScheduler

model_id = "timbrooks/instruct-pix2pix"
pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(model_id, torch_dtype=torch.float16, safety_checker=None)
pipe.to("cuda")
pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)

# Load image
image = Image.open('sd3_large_pix2pix/sd3_large_greek.jpg')

prompt = "Make the balcony wrap around the top story"
num_inference_steps=50
image_guidance_scale = 2
guidance_scale = 10
images = pipe(prompt, image=image,
              num_inference_steps=num_inference_steps,
              image_guidance_scale=image_guidance_scale,
              guidance_scale=guidance_scale
             ).images[0]

images.save(f"sd3_large_pix2pix/sd3_large_greek_balcony.png")