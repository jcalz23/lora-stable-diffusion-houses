export MODEL_NAME="CompVis/stable-diffusion-v1-4"
#export MODEL_NAME="stabilityai/stable-diffusion-xl-base-1.0"
#export DATASET_NAME="lambdalabs/naruto-blip-captions"
#--validation_prompt="Greek modern house with pool" --report_to="wandb" \

accelerate launch --mixed_precision="no" train_text_to_image_lora.py \
  --pretrained_model_name_or_path=$MODEL_NAME \
  --caption_column="text" \
  --resolution=512 --random_flip \
  --train_batch_size=1 \
  --num_train_epochs=50 --checkpointing_steps=5000 \
  --learning_rate=1e-04 --lr_scheduler="constant" --lr_warmup_steps=0 \
  --seed=42 \
  --output_dir="housing-lora" \
  --train_data_dir="/root/lora-stable-diffusion-houses/data/"