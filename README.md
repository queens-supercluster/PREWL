# PREWL

Prompt Engineering Wrapper for LLMs (PREWL): A library for rapidly prototyping LLM-based applications via prompt engineering for NLU.

## Usage

```python
import prewl, json

# Load configuration for backend (e.g., GPT-3 credentials)
prewl.configure("config.json")

# Load the example prompts
examples =  prewl.load_promps("prompts.json")

PATTERN = """
Text: {text}
Sentiment: {sentiment}
"""

# Prompts objects
prompts = prewl.load_prompts(PATTERN, examples, output='sentiment')

# Build the backend-driven model that will be used
model = prewl.train(prompts) # Model object


# Use the model to build a prompt for the LLM, fetch the completion, and parse it
new_input = "This movie was off the hook!"
resp = model.infer(new_input)


print("\n New input: ", new_input)
print("Prediction: ", resp)
print()
```

More examples can be found in the `examples/` directory.

## Contributing

Coming soon...

## Requirements

### Setting up virtual environment

```bash
python -m venv .env
source .env/bin/activate
```

### Installing torch

```bash
pip install torch --extra-index-url https://download.pytorch.org/whl/cu113
```

## Citing This Work

Coming soon...
