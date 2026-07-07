"""
DumbGPT — the dumbest real AI model.

Architecture: character-level Markov chain (order-N).
"Training": counts which letters follow which letter-sequences
in words.txt. No neural net, no gradient descent, no attention.
Just frequency tables. It is, however, a genuine statistical
language model — it just has zero understanding of anything.

Feed it "every English word possible" and it will hallucinate
brand new words that sound plausible but mean nothing.
That's the magic you're imagining: water + lava + eating,
mashed into letter soup like "watava" or "eathunder".
"""

import random
import json
from collections import defaultdict

ORDER = 2  # how many previous characters it "remembers". try 1, 2, or 3.

def train(words, order=ORDER):
    model = defaultdict(lambda: defaultdict(int))
    for word in words:
        padded = ("^" * order) + word + "$"
        for i in range(len(padded) - order):
            context = padded[i:i + order]
            next_char = padded[i + order]
            model[context][next_char] += 1
    return model

def generate_word(model, order=ORDER, max_len=15):
    context = "^" * order
    result = ""
    for _ in range(max_len):
        choices = model.get(context)
        if not choices:
            break
        chars, weights = zip(*choices.items())
        next_char = random.choices(chars, weights=weights)[0]
        if next_char == "$":
            break
        result += next_char
        context = (context + next_char)[-order:]
    return result

def main():
    with open("words.txt") as f:
        words = [w.strip() for w in f if w.strip()]

    print(f"Training DumbGPT on {len(words)} words (order={ORDER} Markov chain)...")
    model = train(words)
    print("Training complete. (This took milliseconds. That's the joke.)\n")

    with open("dumbgpt_model.json", "w") as f:
        json.dump({k: dict(v) for k, v in model.items()}, f)

    print("Sample hallucinations from your trained model:\n")
    for _ in range(15):
        print(" -", generate_word(model))

if __name__ == "__main__":
    main()
