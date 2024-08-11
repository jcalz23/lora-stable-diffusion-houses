from diffusers import StableDiffusionPipeline
from diffusers import DiffusionPipeline
import torch


#pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16)
model_path = "housing-lora"
pipe.unet.load_attn_procs(model_path)
pipe.to("cuda")

#prompt = "This home is a modern cabin in Canadian forest. It features tall windows and dark wood and has an A-frame above the front-door."
prompt = "The facade features beige stucco walls, brown shingle roofing, and white trim. Decorative elements include circular wall art. White planters and minimalistic exterior lighting fixtures are present."
for scale in [1, 0.75, 0.5, 0.25, 0]:
    for i in range(5):
        #image = pipe(prompt, num_inference_steps=100, guidance_scale=15).images[0]
        image = pipe(prompt, num_inference_steps=150, guidance_scale=15, cross_attention_kwargs={"scale": scale}).images[0]
        image.save(f"stucco_50e/image_{scale}_{i}.png")





