from transformers import pipeline, set_seed

generator = pipeline('text-generation', model='gpt2')

set_seed(42)

text_generator = generator("Some Text", max_length=30, num_return_sequences=1)

print(text_generator)
