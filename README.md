# lora-stable-diffusion-houses
Applying LoRA method to fine-tune Stable Diffusion model for images of houses

Goals: 
- Fine-tune Stable Diffusion model for images of houses using LoRA method
- Explore tuning on subset groups of houses to generate multiple LoRA weights

To-Do:
- [x] Select dataset ([Houses-dataset](https://github.com/emanhamed/Houses-dataset/tree/master))

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

- V2 Instructions?
    - Install diffusers
    - Copy requirements file to git
    - Copy py script to git and required utils

SAT
- [-] Get descriptions of houses
    - [x] Define 2-4 prompts per image
    - [x] Write modules to call image model with prompts, save descriptions
    - [x] Run small set
    - [-] Run full set (after LoRA tested)
- [] Get my data into HF format <----- focus here while waiting on quota increase
    - [] Notebook has it pretty close
    - [] Fix collection to use imgs_all and copy imgs to imgs/ after text is prepared
    - [] Test
- [] Fine-tune Stable Diffusion model using LoRA method
    - [x] Find good reference (HF)
    - [x] Run LoRA on SageMaker w sample data
        - [x] Use this setup for each instance: [link](https://github.com/huggingface/diffusers/tree/main/examples/text_to_image#training-with-lora)
        - [x] Move bash script
    - [] Run LoRA on subset
    - [] Run LoRA on full set
- [] Evaluate the quality of the generated images

SUN
- [] Explore tuning on subset groups of houses to generate multiple LoRA weights
- [] Generate images of houses using the subset models
- [] Evaluate the quality of the generated images

Citations
@article{ahmed2016house, title={House price estimation from visual and textual features}, author={Ahmed, Eman and Moustafa, Mohamed}, journal={arXiv preprint arXiv:1609.08399}, year={2016} }