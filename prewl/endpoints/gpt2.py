from prewl.endpoints.base import Endpoint

class GPT2(Endpoint):
    
    def call(self, prompt):
        from transformers import pipeline, set_seed
        generator = pipeline('text-generation', model='gpt2')
        set_seed(42)
        text_generator = generator(prompt, max_length=30, num_return_sequences=1)
        return text_generator
