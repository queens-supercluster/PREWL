# PREWL
Prompt Engineering Wrapper for LLMs (PREWL): A library for rapidly prototyping LLM-based applications via prompt engineering for NLU.

## Usage
```python
import prewl

# Optionally use a config.json
prewl.configure({
    'service'   : 'gpt3', # gpt2, 6b, ...
    'token'     : '12345', # whatever is required for authentication
})

# Optionally load from file
PROMPTS = """
Text: I really don't like this movie.
Sentiment: negative

Text: This flick was sick!
Sentiment: positive

Text: Meh. It was ok. I've seen better, though.
Sentiment: neutral
"""

INPUT_REGEX = "Text: (.+)"
OUTPUT_REGEX = "Sentiment: (.+)"

prompts = prewl.load_prompts(PROMPTS)

model = prewl.train(prompts)

print(model.infer("This movie was off the hook!"))

```

## Contributing
Coming soon...

## Requirements
Coming soon...

## Citing This Work
Coming soon...
