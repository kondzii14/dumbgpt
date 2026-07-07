# DumbGPT 🧠🔥💧

> DumbGPT is Dumbest AI in the world (i think, write in issues if im wrong)

The world's dumbest **real, actually-trained** AI model.

No neural network. No GPU. No attention mechanism. Just a
character-level Markov chain trained on a pile of English words —
and it will happily invent brand new ones that sound plausible
but mean absolutely nothing.

Feed it `water`, `lava`, `eating`, `explosion` and it dreams up
things like `watava`, `lashquake`, `eruptream`.

## Example conversation

```
You: hello
DumbGPT: Sion ead panter eng!

You: what is the meaning of life?
DumbGPT: Sal twingirea dang en vallusher squantaildestro scrain...
```

It never understands a single word you say. That's the point.


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
python chat.py         # chat with it! it will respond in pure hallucination
```

`chat.py` is a real conversational loop — you type, it "replies" — it just
never understands a single word you say. Try `python chat.py --order 1`
for maximum chaos, or `--order 3` for slightly-too-coherent replies.

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

GPL-3.0. Do whatever you want with it — it's letter soup. Just keep it open source.
