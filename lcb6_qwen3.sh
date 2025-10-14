export HF_HUB_CACHE=/home/ubuntu/.cache/huggingface/hub

python -m eval.eval \
    --model hf \
    --tasks LiveCodeBench \
    --model_args 'pretrained=Qwen/Qwen3-8B,parallelize=True' \
    --batch_size 16 \
    --max_tokens 4096 \
    --output_path logs_lcbv6_sample_true_solver_template