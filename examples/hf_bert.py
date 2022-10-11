import prewl, json

#-----------------------------------------#

# Optionally use a config.json
#prewl.configure("config.json")

# Dynamically detect if the argument is json or a file with json
prewl.configure({
    'backend': {
        'service': 'bert-base-uncased',
        'remote': True,
        'token': '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' # Use your huggingface token
    },
    'newline-delimited': True, # Should a new line indicate the end of the completion
    'classes': None, # defaults to None
    'max-length': 3, # output response upper length limit
    'gpu': True, # True or the GPU number you would like to use (if local). False (or -1 if local) indicates CPU,
    'resp_parser': 'mask_fill_parser'
})

#-----------------------------------------#

PROMPTS = """
[
    {
        "text": "I ate popcorn at the movies."
    },

    {
        "text": "This flick was sick!"
    },

    {
        "text": "It was ok. I've seen better, though."
    }
]
"""

examples = json.loads(PROMPTS)

PATTERN = """
{text}
"""

# Prompts objects
prompts = prewl.load_prompts(PATTERN, examples, 'mask')


#-----------------------------------------#

# Creates a function that when called will
#  (1) prompt the server
#  (2) fetch the response
#  (3) returns the parsed result
model = prewl.train(prompts) # Model object

new_input = "This [MASK] was off the hook!"
resp = model.infer(new_input)

print("\n New input: ", new_input)
print("Prediction: ", resp)
print()

