# iLoRA Reproduction Procedure

This document outlines the steps to set up the environment and run the iLoRA code using Docker.

## Prerequisites

- **Docker**: Ensure Docker is installed and running.
- **NVIDIA GPU**: A machine with an NVIDIA GPU is required.
- **NVIDIA Container Toolkit**: Required for Docker to access the GPU.
- **Hugging Face Token**: Required to download the LLaMA-2-7b-hf model.

## 1. Setup Environment

### Build and Start Container
We provide a helper script to build the Docker image and start the container with the necessary configurations (GPU support, shared memory, volume mounting).

```bash
chmod +x start_docker.sh
./start_docker.sh
```

This script will:
1. Build the Docker image `ilora-repro`.
2. Start a container named `ilora-container` in the background.
3. Mount the current directory to `/app` inside the container.
4. Allocate 150GB of shared memory.
5. Expose all GPUs (but the Dockerfile defaults to using GPU 1 via `CUDA_VISIBLE_DEVICES=1`).

### Enter the Container
To run commands inside the container:

```bash
docker exec -it ilora-container bash
```

## 2. Prepare Model

Inside the container, download the LLaMA-2-7b-hf model. You will need your Hugging Face access token.

```bash
# Replace YOUR_HF_TOKEN with your actual token
python download_model.py --token YOUR_HF_TOKEN
```

The model will be downloaded to `./models/Llama-2-7b-hf`.

## 3. Run Training/Evaluation

The repository includes several shell scripts for training and evaluation. You can run them directly inside the container.

**Note**: Before running, ensure the `.sh` scripts point to the correct model path. The `download_model.py` script saves the model to `./models/Llama-2-7b-hf`. You may need to update the `llm_path` argument in the scripts or pass it dynamically.

### Example: Train on MovieLens

```bash
# Update llm_path in train_movielens.sh or run the command manually
sh train_movielens.sh
```

### Example: Evaluate on MovieLens

```bash
sh test_movielens.sh
```

## Troubleshooting

- **GPU Access**: If `nvidia-smi` fails inside the container, ensure the NVIDIA Container Toolkit is installed on the host and the container was started with `--gpus all` (the start script does this).
- **Memory Issues**: If you encounter OOM errors, the 150GB shared memory allocation should help, but you may also need to adjust batch sizes in the training scripts.
