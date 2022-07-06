from prewl.endpoints.base import Endpoint

class GPT2(Endpoint):
    
    def call(self, prompt):
        import tensorflow as tf
        from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
        tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        model = TFGPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id)

        # encode context the generation is conditioned on
        input_ids = tokenizer.encode(prompt, return_tensors='tf')

        # generate text until the output length (which includes the context length) reaches 50
        greedy_output = model.generate(input_ids, max_length=100)

        return tokenizer.decode(greedy_output[0], skip_special_tokens=True)

