import os
import argparse
from huggingface_hub import snapshot_download

def download_model(token=None, output_dir="./models/Llama-2-7b-hf"):
    """
    Downloads the Llama-2-7b-hf model from Hugging Face.
    """
    model_id = "meta-llama/Llama-2-7b-hf"
    
    print(f"Downloading {model_id} to {output_dir}...")
    
    try:
        snapshot_download(
            repo_id=model_id,
            local_dir=output_dir,
            local_dir_use_symlinks=False,
            token=token
        )
        print("Download complete!")
    except Exception as e:
        print(f"Error downloading model: {e}")
        print("Please ensure you have a valid Hugging Face token with access to the Llama-2 models.")
        print("You can set the token via the HF_TOKEN environment variable or pass it as an argument.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download Llama-2-7b-hf model")
    parser.add_argument("--token", type=str, help="Hugging Face access token", default=os.environ.get("HF_TOKEN"))
    parser.add_argument("--output_dir", type=str, default="./models/Llama-2-7b-hf", help="Directory to save the model")
    
    args = parser.parse_args()
    
    if not args.token:
        print("Warning: No Hugging Face token provided. The download may fail if the model is gated.")
        
    download_model(token=args.token, output_dir=args.output_dir)
