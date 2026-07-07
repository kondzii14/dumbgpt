"""
DumbGPT Chat — a real chat interface to the dumbest real AI model.

You type a message. DumbGPT completely ignores its meaning and
responds with a sentence built out of hallucinated words sampled
from its trained Markov chain. It's a real conversational loop,
a real trained model, and a real 0% chance of coherence.
"""

import random
import json
import argparse
from train import generate_word, ORDER

def load_model(path="dumbgpt_model.json"):
    with open(path) as f:
        return json.load(f)

def hallucinate_sentence(model, order=ORDER, min_words=3, max_words=9):
    n = random.randint(min_words, max_words)
    words = [generate_word(model, order=order) for _ in range(n)]
    words = [w if w else "uh" for w in words]  # guard against empty generations
    sentence = " ".join(words)
    sentence = sentence[0].upper() + sentence[1:]
    ending = random.choice([".", ".", ".", "!", "?", "..."])
    return sentence + ending

def maybe_reaction(user_input):
    """Cheap flavor: react to punctuation/length like a 'real' chatbot would, without
    understanding a single word of what was actually said."""
    if user_input.strip().endswith("?"):
        return random.choice(["Hmm. ", "Well... ", ""])
    if len(user_input.split()) > 15:
        return random.choice(["Wow, okay. ", "That's a lot. ", ""])
    return ""

def main():
    parser = argparse.ArgumentParser(description="Chat with DumbGPT.")
    parser.add_argument("--order", type=int, default=ORDER,
                         help="Markov chain order (1=max chaos, 3=almost words)")
    parser.add_argument("--model", type=str, default="dumbgpt_model.json")
    args = parser.parse_args()

    model = load_model(args.model)

    print("=" * 50)
    print(" DumbGPT Chat v1.0")
    print(" A real AI model that only hallucinates.")
    print(" Type 'quit' to exit.")
    print("=" * 50)

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nDumbGPT: gorf.")
            break

        if user_input.lower() in ("quit", "exit"):
            print("DumbGPT: velethast.")
            break
        if not user_input:
            continue

        reply = maybe_reaction(user_input) + hallucinate_sentence(model, order=args.order)
        print(f"DumbGPT: {reply}")

if __name__ == "__main__":
    main()
