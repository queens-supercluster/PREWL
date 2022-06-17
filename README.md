# PREWL

Prompt Engineering Wrapper for LLMs (PREWL): A library for rapidly prototyping LLM-based applications via prompt engineering for NLU.

## Usage

```python
import prewl, json


#-----------------------------------------#

# Optionally use a config.json
# prewl.configure("config.json")

# Dynamically detect if the argument is json or a file with json
prewl.configure({
    'backend': {
        'service'   : 'gpt3', # gpt2, 6b, ...
        'token'     : '12345', # whatever is required for authentication
    },
    'repeat-limit': 10, # if making repeated requests, no more than 10
    'newline-delimited': True, # Should a new line indicate the end of the completion
    'classes': ['positive', 'negative', 'neutral'], # defaults to None
})


#-----------------------------------------#

PROMPTS = """
[
    {
        "text": "I really don't like this movie.",
        "sentiment": "negative"
    },

    {
        "text": "This flick was sick!",
        "sentiment": "positive"
    },

    {
        "text": "It was ok. I've seen better, though.",
        "sentiment": "neutral"
    }
]
"""

prompt_config = json.loads(PROMPTS)

PATTERN = """
Text: {text}
Sentiment: {sentiment}
"""

# Prompts objects
prompts = prewl.load_prompts(prompt_config, PATTERN)

# Optionally load prompts from file
# prompts = prewl.load_prompts("prompts.txt", INPUT_REGEX, OUTPUT_REGEX)

# Optionally use a custom method
def check_for_positive(resp):
    return "positive" in resp
# prompts = prewl.load_prompts(PROMPTS, INPUT_REGEX, check_for_positive)

#-----------------------------------------#

# Creates a function that when called will
#  (1) prompt the server
#  (2) fetch the response
#  (3) returns the parsed result
model = prewl.train(prompts) # Model object

print(model.infer("This movie was off the hook!")) # Response should be True or "positive"

```

## Contributing

Coming soon...

## Requirements

Coming soon...

## Citing This Work

Coming soon...
