"""Load the trained DumbGPT model and generate new hallucinated words."""
import json
import random
from train import generate_word, ORDER

def load_model(path="dumbgpt_model.json"):
    with open(path) as f:
        raw = json.load(f)
    return {k: v for k, v in raw.items()}

if __name__ == "__main__":
    model = load_model()
    n = 20
    print(f"DumbGPT v1.0 — {n} freshly hallucinated words:\n")
    for _ in range(n):
        print(" -", generate_word(model))
