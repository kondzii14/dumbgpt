# DumbGPT 🧠🔥💧

The world's dumbest **real, actually-trained** AI model.

No neural network. No GPU. No attention mechanism. Just a
character-level Markov chain trained on a pile of English words —
and it will happily invent brand new ones that sound plausible
but mean absolutely nothing.

Feed it `water`, `lava`, `eating`, `explosion` and it dreams up
things like `watava`, `lashquake`, `eruptream`.

## How it works

1. `words.txt` — a curated list of ~400 English words across categories
   (nature, animals, actions, science, food, objects, weather...).
2. `train.py` — "trains" a model by counting which letters follow which
   letter-sequences in the word list. This is a real, legitimate
   statistical language model (the same family of idea behind old-school
   text predictors) — it's just tiny and has zero semantic understanding.
3. `generate.py` — samples new "words" from the trained model.

## Usage

```bash
python train.py       # trains the model, saves dumbgpt_model.json, prints samples
python generate.py    # generates more hallucinations from the saved model
```

## Tuning the dumbness

Open `train.py` and change `ORDER`:
- `ORDER = 1` → nearly random letter soup (maximum dumb)
- `ORDER = 2` → default, plausible-sounding nonsense
- `ORDER = 3` → starts sounding suspiciously like real words (too smart, not allowed)

## Add your own words

Add more words to `words.txt` (one per line, or space-separated) and
re-run `train.py` — more data, still zero comprehension.

## Benchmarks

| Model      | Params | Training time | Understands anything |
|------------|--------|----------------|------------------------|
| GPT-4      | ~1.7T  | months         | debatable              |
| DumbGPT    | 0      | milliseconds   | no                     |

## License

MIT. Do whatever you want with it — it's letter soup.
