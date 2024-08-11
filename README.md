# lora-stable-diffusion-houses
Applying LoRA method to fine-tune Stable Diffusion model for images of houses

For full write-up see: https://medium.com/@j.calzaretta.ai/advancements-in-ai-image-generation-a-look-at-lora-and-instructpix2pix-998e7c6598a4

Goals: 
- Fine-tune Stable Diffusion model for images of houses using LoRA method
- Explore image editing with InstructPix2Pix

SageMaker Setup
- Instance: g4dn.4xlarge
- Instructions
git clone https://github.com/huggingface/diffusers
cd diffusers
pip install .
cd examples/text_to_image/
pip install -r requirements.txt
accelerate config
huggingface-cli login

Tasks (for my tracking)
- [x] Select dataset ([Houses-dataset](https://github.com/emanhamed/Houses-dataset/tree/master))

SAT
- [x] Get descriptions of houses via GPT4o
- [x] Get my data into HF format
- [x] Fine-tune Stable Diffusion model using LoRA method
- [x] Evaluate the quality of the generated images

SUN
- [x] Explore InstructPix2Pix
- [x] Eval results

MON
- [x] Write blog

NEXT
- [] Clean up code base

Citations
@article{ahmed2016house, title={House price estimation from visual and textual features}, author={Ahmed, Eman and Moustafa, Mohamed}, journal={arXiv preprint arXiv:1609.08399}, year={2016} }
