export HF_HUB_CACHE=/home/ubuntu/.cache/huggingface/hub

# accelerate launch --num-processes 8 --num-machines 1 \
#     --multi-gpu -m eval.eval \
#     --model hf \
#     --tasks LiveCodeBench \
#     --model_args 'pretrained=Qwen/Qwen2.5-7B-Instruct,tensor_parallel_size=2' \
#     --batch_size 1 \
#     --max_tokens 4096 \
#     --output_path logs_qwen25_7b_instruct_lcb \

python -m eval.eval \
    --model hf \
    --tasks LiveCodeBench \
    --model_args 'pretrained=Qwen/Qwen2.5-7B-Instruct,parallelize=True' \
    --batch_size 16 \
    --max_tokens 4096 \
    --output_path logs_qwen25_7b_instruct_lcb